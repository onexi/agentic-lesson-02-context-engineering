"""Small helpers for running tests written as ordinary functions."""


def expect_value_error(function, *args):
    """Call a function and return its error message; fail if it accepts the input."""
    try:
        function(*args)
    except ValueError as error:
        return str(error)
    raise AssertionError("Expected ValueError, but the input was accepted")


def run_tests(tests):
    """Run every listed test, print its result, and exit with an error if any fail."""
    failures = 0
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
        except Exception as error:
            failures += 1
            print(f"FAIL: {test.__name__}: {type(error).__name__}: {error}")

    print(f"{len(tests) - failures}/{len(tests)} tests passed")
    if failures:
        raise SystemExit(1)
    print("OK")
