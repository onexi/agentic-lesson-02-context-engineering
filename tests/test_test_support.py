"""Maintainer checks for the test runner; no classes or extra dependencies."""

from contextlib import redirect_stdout
from io import StringIO
import subprocess
import sys

from test_support import expect_value_error, run_tests


def capture_run(tests):
    output = StringIO()
    exit_code = 0
    with redirect_stdout(output):
        try:
            run_tests(tests)
        except SystemExit as error:
            exit_code = error.code
    return exit_code, output.getvalue()


def test_success_reports_ok():
    def passing_check():
        pass

    code, output = capture_run([passing_check])
    assert code == 0
    assert "1/1 tests passed" in output
    assert output.endswith("OK\n")


def test_failure_runs_remaining_checks_and_exits_nonzero():
    visited = []

    def failing_check():
        raise AssertionError("incorrect result")

    def later_check():
        visited.append("ran")

    code, output = capture_run([failing_check, later_check])
    assert code == 1
    assert visited == ["ran"]
    assert "incorrect result" in output
    assert "1/2 tests passed" in output
    assert "OK" not in output


def test_unexpected_exception_is_a_failure():
    def broken_check():
        raise RuntimeError("unexpected problem")

    code, output = capture_run([broken_check])
    assert code == 1
    assert "RuntimeError: unexpected problem" in output
    assert "OK" not in output


def test_empty_suite_is_rejected():
    code, output = capture_run([])
    assert code != 0
    assert "OK" not in output


def test_optimized_python_is_rejected():
    for option in ("-O", "-OO"):
        result = subprocess.run(
            [sys.executable, option, "-c",
             "from test_support import run_tests; run_tests([lambda: None])"],
            capture_output=True, text=True,
        )
        assert result.returncode != 0
        assert "OK" not in result.stdout


def test_expected_error_returns_message():
    def reject(value):
        raise ValueError(f"invalid {value}")

    assert expect_value_error(reject, "input") == "invalid input"


def test_accepted_input_does_not_satisfy_error_check():
    def accept(value):
        return value

    try:
        expect_value_error(accept, 10)
    except AssertionError:
        return
    raise AssertionError("The helper incorrectly accepted a missing ValueError")


def test_wrong_exception_is_not_accepted_as_value_error():
    def broken():
        raise TypeError("wrong exception")

    try:
        expect_value_error(broken)
    except TypeError:
        return
    raise AssertionError("The helper swallowed the wrong exception")


if __name__ == "__main__":
    run_tests([
        test_success_reports_ok,
        test_failure_runs_remaining_checks_and_exits_nonzero,
        test_unexpected_exception_is_a_failure,
        test_empty_suite_is_rejected,
        test_optimized_python_is_rejected,
        test_expected_error_returns_message,
        test_accepted_input_does_not_satisfy_error_check,
        test_wrong_exception_is_not_accepted_as_value_error,
    ])
