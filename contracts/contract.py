# Copyright 2017 Benoit Bernard All Rights Reserved.

"""
Module containing code contracts.
"""

import re
import traceback
from collections import Iterable

# Regex used to extract the name of the variable passed as the first parameter to the
# contract function.
_MATCH_FIRST_PARAMETER_REGEX = re.compile(r"\(([\w.]+)[,)]")


def is_not_none(value):
    """
    Checks that the specified value is not equal to None.

    :param value: the value to check.
    :raises: :class:`TypeError` if the value is equal to None.
    """
    if value is None:
        raise TypeError("{0} was equal to None.".format(_get_parameter_name()))


def is_not_empty(value):
    """
    Checks that the specified value is not empty.

    :param value: the value to check. To be considered empty, it must be equal to None, or equal to "" if it's a string.
                  If it's an :class:`~collections.Iterable` object, its length must be equal to 0. Any other object type
                  will never be considered empty.
    :raises: :class:`ValueError` if the value is considered empty.
    """
    if value is None or (type(value) is str and not value) or (isinstance(value, Iterable) and len(value) == 0):
        raise ValueError("{0} was empty.".format(_get_parameter_name()))


def is_equal_to_any(value, expected_values, expression_str=None):
    """
    Checks that the specified value is equal to at least one of the expected values.

    :param value: the value to check.
    :param expected_values: an :class:`~collections.Iterable` object containing the expected values.
    :param expression_str: (optional) a string representing the evaluated boolean expression (e.g. 'b > c').
    :raises: :class:`ValueError` if the value is not equal to any of the expected values.
    """
    if value not in expected_values:
        raise ValueError(
            "{0} with value {1} and type {2} was not equal to any of the expected values.".format(expression_str if expression_str else _get_parameter_name(),
                                                                                                  str(value),
                                                                                                  type(value).__name__))


def is_true(value, expression_str=None):
    """
    Checks that the specified value is equal to True.

    :param value: the value to check. It can be a standard variable's value, or the result of an evaluated boolean
                  expression (e.g. a or b > c).
    :param expression_str: (optional) a string representing the evaluated boolean expression (e.g. 'b > c').
    :raises: :class:`TypeError` if the value is not True.
    """
    if value is not True:
        raise ValueError("{0} was not True.".format(expression_str if expression_str else _get_parameter_name()))


def is_false(value, expression_str=None):
    """
    Checks that the specified value is equal to False.

    :param value: the value to check. It can be a standard variable's value, or the result of an evaluated boolean
                  expression (e.g. a or b > c).
    :param expression_str: (optional) a string representing the evaluated boolean expression (e.g. 'b > c').
    :raises: :class:`TypeError` if the value is not False.
    """
    if value is not False:
        raise ValueError("{0} was not False.".format(expression_str if expression_str else _get_parameter_name()))


def is_equal(value, expected_value, expression_str=None):
    """
    Checks that the specified value is strictly equal to the expected value.

    :param value: the value to check.
    :param expected_value: the expected value.
    :param expression_str: (optional) a string representing the evaluated boolean expression (e.g. 'len(a) == 1').
    :raises: :class:`ValueError` if the values are not strictly equal.
    """
    if value != expected_value:
        raise ValueError(
            "{0} with value {1} was not equal to {2}.".format(
                expression_str if expression_str else _get_parameter_name(),
                value, expected_value))


def is_greater_than(value, expected_value):
    """
    Checks that the specified value is greater than the expected value.

    :param value: the value to check.
    :param expected_value: the expected value.
    :raises: :class:`ValueError` if the value is not greater than the expected value.
    """
    if value <= expected_value:
        raise ValueError(
            "{0} with value {1} was not greater than {2}.".format(_get_parameter_name(), value, expected_value))


def is_greater_than_or_equal(value, expected_value):
    """
    Checks that the specified value is greater than or strictly equal to the expected value.

    :param value: the value to check.
    :param expected_value: the expected value.
    :raises: :class:`ValueError` if the value is not greater than or strictly equal to the expected value.
    """
    if value < expected_value:
        raise ValueError("{0} with value {1} was not greater than or equal to {2}.".format(_get_parameter_name(), value,
                                                                                           expected_value))


def all_have_attribute(value, attribute_name):
    """
    Checks that all objects contained in value - be it a single object or an :class:`~collections.Iterable` of objects -
    have the specified attribute.

    :param value: the value to check. It can be a single object, or an an :class:`~collections.Iterable` of objects.
    :param attribute_name: a string containing the name of the attribute to look for.
    :raises: :class:`AttributeError` if one of the objects does not contain the specified attribute.
    """
    if isinstance(value, Iterable):
        for item in value:
            if not hasattr(item, attribute_name):
                raise AttributeError("{0} contains an item of type {1} not having the expected attribute '{2}'.".format(
                    _get_parameter_name(), type(item).__name__, attribute_name))
    elif not hasattr(value, attribute_name):
        raise AttributeError(
            "{0} with type {1} does not have the expected attribute '{2}'.".format(_get_parameter_name(),
                                                                                   type(value).__name__,
                                                                                   attribute_name))


def all_have_method(value, method_name):
    """
    Checks that all objects contained in value - be it a single object or an :class:`~collections.Iterable` of objects -
    have the specified method.

    :param value: the value to check. It can be a single object, or an an :class:`~collections.Iterable` of objects.
    :param method_name: a string containing the name of the method to look for.
    :raises: :class:`AttributeError` if one of the objects does not contain the specified method.
    """
    if isinstance(value, Iterable):
        for item in value:
            if not (hasattr(item, method_name) and callable(getattr(item, method_name))):
                raise AttributeError("{0} contains an item of type {1} not having the expected method '{2}'.".format(
                    _get_parameter_name(), type(item).__name__, method_name))
    elif not (hasattr(value, method_name) and callable(getattr(value, method_name))):
        raise AttributeError("{0} with type {1} does not have the expected method '{2}'.".format(_get_parameter_name(),
                                                                                                 type(value).__name__,
                                                                                                 method_name))


def is_callable(value):
    """
    Checks that the specified value is a callable object (i.e. has a '__call__' attribute).

    :param value: the value to check.
    :raises: :class:`TypeError` if the value is not a callable object.
    """
    if not hasattr(value, '__call__'):
        raise TypeError("{0} with type {1} was not callable.".format(_get_parameter_name(), type(value).__name__))


def is_instance(value, cls):
    """
    Checks that the specified value is an instance of the given class.

    :param value: the value to check.
    :param cls: the expected class of the value.
    :raises: :class:`TypeError` if the value is not an instance of the class.
    """
    if not isinstance(value, cls):
        raise TypeError("{0} was not an instance of {1}.".format(_get_parameter_name(), cls.__name__))


def _get_parameter_name():
    # Retrieve the line of code that performed the call to the contract function.
    stack = traceback.extract_stack()
    _, _, _, code = stack[-3]

    # 'code' will contain something like this:
    #   'contract.is_not_none(a, expression)'
    #
    # So we extract the name of the first variable ('a') to generate a more specific, meaningful error message.
    match = _MATCH_FIRST_PARAMETER_REGEX.search(code)
    if not match:
        raise Exception("The call to the code contract had an unexpected format.")
    return match.groups(0)[0]
