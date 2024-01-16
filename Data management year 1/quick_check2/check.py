'''check: a unit-testing module for introductory programming courses.

This module provides a simple unit-testing facility, in the spirit of the
testing forms provided by the student languages in "How to Design Programs,
Second Edition".

The functions provided by this module are:

    equal - test if two objects are equal. For two objects to be equal,
        they must have the same type and be comparable by ==. Print a
        descriptive message if the test fails.

    within - test if two floats or an int and a float differ by a
        specified amount. Print a descriptive message if the test fails.

    summary - print a short report about the number of number of tests run and
        the number of failed tests.

Example: testing Python's built-in abs function.

import check

def test_abs_int() -> None:
    """Test abs with integer arguments."""
    check.equal(abs(0), 0)
    check.equal(abs(-1), 1)
    check.equal(abs(1), 1)
    check.summary()

def test_abs_float() -> None:
    """Test abs with float arguments."""
    check.within(abs(0.0), 0.0, 0.0001)
    check.within(abs(-1.0), 1.0, 0.0001)
    check.within(abs(1.0), 1.0, 0.0001)
    check.within(abs(-0.1 - 0.1 - 0.1), 0.3, 0.0001)
    check.summary()

test_abs_int()
test_abs_float()
'''

import os
import linecache
import inspect

__author__ = 'D. L. Bailey, SCE, Carleton University'
__version__ = '1.04'
__date__ = 'Mar. 12, 2023'

"""
History:
1.02 Jan. 24, 2020, DLB

Added lots of comments to print_check_location(), to explain how it rummages
around the activation frames to obtain information about the failed test.

1.03 Jan. 28, 2021, DLB

equal(): if outcome or expected are strings and the check fails,
enclose the strings in quotes in the failure report.

Added tally() and score(): a quick hack to support grading students' code.

1.04 Mar. 12, 2023, DLB

Deleted tally() and score().

summary() no longer clears the counters that keep track of the number of
tests run and the number of failed tests, by default.

equal() and within(): the optional message is now printed before the
information about the check call that failed.

Renamed print_check_location to _print_failed_check_expression.
"""

_num_tests_run = 0
_num_tests_failed = 0


def equal(outcome, expected, message: str = '') -> None:
    '''Check if outcome and expected have same type and are equal (as determined
    by the == operator), and print a descriptive report if the check fails.

    Typically, parameter outcome is the value returned by a call expression,
    and expected is the value we expect a correct implementation of the
    called function to return.

    Optional parameter message can be used to provide a summary description
    of the test or information that helps us interpret the results.

    This function shouldn't be used if outcome or expected evaluate to a float;
    instead, use within to test if outcome is "close-enough" to expected for the
    two values to be considered equal. Similarly, this function shouldn't be
    used to test two objects that contain floats (e.g., lists, tuples, sets,
    dicts, etc.) for equality.
    '''
    global _num_tests_run, _num_tests_failed

    _num_tests_run += 1
    outcome_type = type(outcome)
    expected_type = type(expected)

    if outcome_type != expected_type or outcome != expected:
        _num_tests_failed += 1
        print("FAILED: check.equal")

        if message != '':
            print(message)

        _print_failed_check_expression()

        if outcome_type != expected_type:
            print("failure: outcome, {0}, has type {1}, but expected value, {2}, has type {3}".
                  format(outcome, str(outcome_type).strip('<class> '), expected, str(expected_type).strip('<class> ')))
        else:  # types match, but outcome != expected
            print("failure: outcome, {0}, differs from expected value, {1}".format(repr(outcome), repr(expected)))
        print('----')


def within(outcome: float, expected: float, epsilon: float, message: str = '') -> None:
    '''Check if outcome and expected differ by at most epsilon, and print a
    descriptive report if the check fails.

    At least one of outcome and expected must have type float.
    If outcome is a float, expected can be a float or an int.
    If expected is a float, outcome can be a float or an int.

    Typically, parameter outcome is the value returned by a call expression,
    and expected is the value we expect a correct implementation of the
    function to return.

    Optional parameter message can be used to provide a summary description
    of the test or information that helps us interpret the results.
    '''
    global _num_tests_run, _num_tests_failed

    _num_tests_run += 1
    outcome_type = type(outcome)
    expected_type = type(expected)

    # Ensure that we're comparing two floats or an int and a float.
    types_ok = (outcome_type == float and expected_type in (int, float) or
                expected_type == float and outcome_type in (int, float))

    if types_ok and abs(outcome - expected) <= epsilon:
        return

    _num_tests_failed += 1
    print("FAILED: check.within")
    if message != '':
        print(message)

    _print_failed_check_expression()

    if not types_ok:
        print("failure: outcome, {0}, has type {1}; expected value, {2}, has type {3}".
              format(outcome, str(outcome_type).strip('<class> '), expected, str(expected_type).strip('<class> ')))
    else:  # outcome isn't close enough to the expected result
        print("failure: outcome, {0}, differs from expected value, {1}, by more than {2}".
              format(outcome, expected, epsilon))
    print('----')


def summary(clear_counters: bool = False) -> None:
    '''Print the number of tests run and the number of failed tests.

    By default, these counts are retained after they are printed; i.e.,
    repeated calls to summary() will print cumulative counts.
    To clear both counts after they are printed, call summary(True).
    '''
    global _num_tests_run, _num_tests_failed

    print("Ran {0} tests, {1} failed".format(_num_tests_run, _num_tests_failed))
    if clear_counters:
        _num_tests_run = 0
        _num_tests_failed = 0


def _print_failed_check_expression():
    '''Print the filename and line number containing the call to the check
    function that failed and called this function; i.e., called
    _print_failed_check_expression.
    If the check was called by a function, also print that function name.
    Finally, print the call expression that failed.
    '''
    try:
        # See the note regarding keeping references to frame objects in the
        # documentation for Python's inspect module, section "The interpreter
        # stack".

        # currentframe() returns the frame object for
        # _print_failed_check_expression.
        # currentframe().f_back is the frame for the check function that
        # called _print_failed_check_expression.
        # currentframe().f_back.f_back is the frame for the code that called
        # the check function.

        frame = inspect.currentframe().f_back.f_back
        traceback = inspect.getframeinfo(frame)

        # Get the name of the function containing the expression that called
        # the check function, or '<module>' if the call expression is
        # outside of a function definition.

        function_name = traceback.function  # same as frame.f_code.co_name

        # Get the line number (within the source file) of the call.

        lineno = traceback.lineno  # same as frame.f_lineno

        # Either of these two statements should give us the full pathname of
        # the module that contains the call to the check function:
        #     filename = traceback.filename
        #     filename = frame.f_code.co_filename
        #
        # If M.py contains the call and is run as a script:
        #
        #     python -m M
        #
        # both assignment statements will bind filename to the pathname, which
        # will end with 'M.py'.
        #
        # But, when Wing 101 is used to run M.py as __main__,
        # both statements bind filename to a string that starts with
        # "x-wingide-python-shell:", followed by slashes and numbers.
        #
        # The simplest work-around I've found is to grab the full pathname
        # from the frame's f_globals dictionary.

        filename = frame.f_globals['__file__']
        source_lines = linecache.getlines(filename)

        # When displaying the filename, discard everything but the last
        # component in the path.

        print("location: {0}, line {1}".format(os.path.basename(filename), lineno), end='')
        if function_name != '<module>':
            print(", function {0}".format(function_name), end='')
        print("\nexpression: {0}".format(source_lines[lineno - 1].strip()))
    finally:
        del frame
