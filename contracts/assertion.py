# Copyright 2017 Benoit Bernard All Rights Reserved.

"""
Module containing code assertions.

It complements the assertions already available in the :class:`~unittest.TestCase` class.
"""


def does_not_raise(exception_cls, callable_obj, *args, **kwargs):
    """
    Asserts that the specified callable object does not raise an exception of the specified class when called.

    :param exception_cls: the class of the exception.
    :param callable_obj: the callable object (function or method).
    :param args: the positional arguments to pass to the callable.
    :param kwargs: the keyword arguments to pass to the callable.
    :raises: :class:`AssertionError` if the callable raises an exception of the specified class.
    """
    try:
        callable_obj(*args, **kwargs)
    except Exception as e:
        # isinstance() checks for any class in the inheritance chain of the specified class.
        if isinstance(e, exception_cls):
            raise AssertionError("{0} raised by {1}().".format(exception_cls.__name__, callable_obj.__name__))


def raises(exception_cls, callable_obj, *args, **kwargs):
    """
    Asserts that the specified callable object raises an exception of the specified class when called.

    Can be used instead of :meth:`~unittest.TestCase.assertRaises` for consistency across unit tests,
    especially when :func:`~contracts.assertion.does_not_raise` is also used.

    :param exception_cls: the class of the exception.
    :param callable_obj: the callable object (function or method).
    :param args: the positional arguments to pass to the callable.
    :param kwargs: the keyword arguments to pass to the callable.
    :raises: :class:`AssertionError` if the callable does not raise an exception of the specified class.
    """
    raises_with_msg(exception_cls, callable_obj, None, *args, **kwargs)


def raises_with_msg(exception_cls, callable_obj, expected_exception_msg, *args, **kwargs):
    """
    Asserts that the specified callable object raises an exception of the specified type with the specified message
    when called.

    :param exception_cls: the class of the exception.
    :param callable_obj: the callable object (function or method).
    :param expected_exception_msg: the expected substring in the exception's message.
    :param args: the positional arguments to pass to the callable.
    :param kwargs: the keyword arguments to pass to the callable.
    :raises: :class:`AssertionError` if the callable does not raise an exception of the specified class.
    """
    has_raised_expected_error = False
    try:
        callable_obj(*args, **kwargs)
    except Exception as e:
        # isinstance checks for any class in the inheritance chain of the specified class.
        if isinstance(e, exception_cls):
            # If a specific error message is expected, we compare it to the error message contained in the exception.
            # Otherwise, just having caught the expected exception type is enough.
            has_raised_expected_error = expected_exception_msg in str(e) if expected_exception_msg else True

    if not has_raised_expected_error:
        # Include the expected error message if applicable.
        exception_description = exception_cls.__name__ if not expected_exception_msg else "{0} with message '{1}'".format(
            exception_cls.__name__, expected_exception_msg)
        raise AssertionError("{0} was not raised by {1}().".format(exception_description, callable_obj.__name__))


def not_called_with(mock_obj, *args, **kwargs):
    """
    Asserts that the specified mock object was never called with a specific sequence of arguments.

    Acts as a complementary function, because there is no :meth:`assert_not_called_with` method available in the
    :class:`~unittest.mock.Mock` class.

    :param mock_obj: :class:`~unittest.mock.Mock` object.
    :param args: the positional arguments to pass to the callable.
    :param kwargs: the keyword arguments to pass to the callable.
    :raises: :class:`AssertionError` if the callable does not raise an exception of the specified class.
    """
    try:
        mock_obj.assert_any_call(*args, **kwargs)
    except AssertionError:
        # The method was not called with the specified arguments, so everything is good.
        return

    # The method was called with the specified arguments, so raise an error.
    arguments_as_strings = []
    if len(args) > 0:
        arguments_as_strings.append(", ".join([str(arg) for arg in args]))
    if len(kwargs) > 0:
        arguments_as_strings.append(", ".join(["{0}={1}".format(key, value) for key, value in kwargs.items()]))

    raise AssertionError("Function was unexpectedly called with ({0}).".format(", ".join(arguments_as_strings)))


def contains_one_element_of_class(obj_cls, iterable_obj):
    """
    Asserts that the specified iterable object contains one and only one element of the specified class.

    :param obj_cls: the class of the object that is expected to be found in the iterable.
    :param iterable_obj: :class:`~collections.abc.Iterable` object.
    :raises: :class:`AssertionError` if the callable does not raise an exception of the specified class.
    """
    if len(iterable_obj) != 1 or type(iterable_obj[0]) is not obj_cls:
        raise AssertionError(
            "Iterable should contain one and only one object of class '{0}'.".format(obj_cls.__name__))
