# Copyright 2017 Benoit Bernard All Rights Reserved.

import unittest
from contracts import assertion
from contracts import contract


class ContractsTests(unittest.TestCase):
    """
    Class containing unit tests that validate the behavior of contracts.
    """

    def test_is_not_none(self):
        assertion.raises_with_msg(TypeError, _is_not_none_test_method, "a was equal to None.", None)
        assertion.does_not_raise(TypeError, _is_not_none_test_method, "123")

    def test_is_not_none_on_xth_parameter(self):
        assertion.raises_with_msg(TypeError, _is_not_none_on_xth_parameter_test_method, "a was equal to None.", None,
                                  "def", "ghi")
        assertion.raises_with_msg(TypeError, _is_not_none_on_xth_parameter_test_method, "b was equal to None.", "abc",
                                  None, "ghi")
        assertion.raises_with_msg(TypeError, _is_not_none_on_xth_parameter_test_method, "c was equal to None.", "abc",
                                  "def", None)

    def test_is_not_empty(self):
        assertion.raises_with_msg(ValueError, _is_not_empty_test_method, "a was empty.", None)
        assertion.raises_with_msg(ValueError, _is_not_empty_test_method, "a was empty.", "")
        assertion.raises_with_msg(ValueError, _is_not_empty_test_method, "a was empty.", [])
        assertion.does_not_raise(TypeError, _is_not_empty_test_method, "123")
        assertion.does_not_raise(TypeError, _is_not_empty_test_method, [123])

    def test_is_equal_to_any(self):
        assertion.raises_with_msg(ValueError, _is_equal_to_any_test_method,
                                  "a with value 4 and type int was not equal to any of the expected values.", 4,
                                  [1, 2, 3])
        assertion.raises_with_msg(ValueError, _is_equal_to_any_test_method,
                                  "something.abc with value 4 and type int was not equal to any of the expected values.",
                                  4, [1, 2, 3], "something.abc")
        assertion.does_not_raise(ValueError, _is_equal_to_any_test_method, 1, [1, 2, 3])

    def test_is_true(self):
        assertion.raises_with_msg(ValueError, _is_true_test_method, "a > 0 was not True.", -1, "a > 0")
        assertion.does_not_raise(ValueError, _is_true_test_method, 1)

    def test_is_false(self):
        assertion.raises_with_msg(ValueError, _is_false_test_method, "a > 0 was not False.", 1, "a > 0")
        assertion.does_not_raise(ValueError, _is_false_test_method, -1)

    def test_is_equal(self):
        assertion.raises_with_msg(ValueError, _is_equal_test_method, "a with value 2 was not equal to 1.", 2, 1)
        assertion.raises_with_msg(ValueError, _is_equal_test_method, "self.a with value 2 was not equal to 1.", 2, 1,
                                  "self.a")
        assertion.raises_with_msg(ValueError, _is_equal_test_method, "len(tuple) with value 2 was not equal to 1.",
                                  len((1, 2)), 1, "len(tuple)")
        assertion.does_not_raise(ValueError, _is_equal_test_method, 1, 1)
        assertion.does_not_raise(ValueError, _is_equal_test_method, "", "")

    def test_is_greater_than(self):
        assertion.raises_with_msg(ValueError, _is_greater_than_test_method, "a with value 1 was not greater than 2.", 1,
                                  2)
        assertion.does_not_raise(ValueError, _is_greater_than_test_method, 2, 1)

    def test_is_greater_than_or_equal(self):
        assertion.raises_with_msg(ValueError, _is_greater_than_or_equal_test_method,
                                  "a with value 1 was not greater than or equal to 2.", 1, 2)
        assertion.does_not_raise(ValueError, _is_greater_than_or_equal_test_method, 2, 1)

    def test_all_have_attribute(self):
        assertion.raises_with_msg(AttributeError, _all_have_attribute_test_method,
                                  "a with type _TestClsWithMethodAndAttributes does not have the expected attribute 'dummy'.",
                                  _TestClsWithMethodAndAttributes(), "dummy")

        assertion.does_not_raise(AttributeError, _all_have_attribute_test_method, _TestClsWithMethodAndAttributes(),
                                 "a")
        assertion.does_not_raise(AttributeError, _all_have_attribute_test_method, [_TestClsWithMethodAndAttributes(), _TestClsWithMethodAndAttributes()],
                                 "a")

    def test_all_have_method(self):
        assertion.raises_with_msg(AttributeError, _all_have_method_test_method,
                                  "a with type _TestClsWithMethodAndAttributes does not have the expected method 'dummy'.",
                                  _TestClsWithMethodAndAttributes(), "dummy")

        assertion.does_not_raise(AttributeError, _all_have_attribute_test_method, _TestClsWithMethodAndAttributes(),
                                 "my_method")
        assertion.does_not_raise(AttributeError, _all_have_attribute_test_method,
                                 [_TestClsWithMethodAndAttributes(), _TestClsWithMethodAndAttributes()], "my_method")

    def test_is_callable(self):
        assertion.raises_with_msg(TypeError, _is_callable_test_method, "a with type str was not callable", "dummy")
        assertion.does_not_raise(TypeError, _is_callable_test_method, _TestClsWithMethodAndAttributes().my_method)

    def test_is_instance(self):
        # Check that True is an instance of bool.
        try:
            _is_instance_test_method(True, bool)
        except TypeError:
            self.fail("True should be an instance of bool.")

        # Check that True isn't an instance of str.
        try:
            _is_instance_test_method(True, str)
        except TypeError as e:
            self.assertEqual(str(e), "a was not an instance of str.")
            return
        self.fail("True should not be an instance of str.")


def _is_not_none_test_method(a):
    contract.is_not_none(a)


def _is_not_none_on_xth_parameter_test_method(a, b, c):
    contract.is_not_none(a)
    contract.is_not_none(b)
    contract.is_not_none(c)


def _is_not_empty_test_method(a):
    contract.is_not_empty(a)


def _is_equal_to_any_test_method(a, expected_values, expression=None):
    contract.is_equal_to_any(a, expected_values, expression)


def _is_true_test_method(a, expression=None):
    contract.is_true(a > 0, expression)


def _is_false_test_method(a, expression=None):
    contract.is_false(a > 0, expression)


def _is_equal_test_method(a, expected_value, expression=None):
    contract.is_equal(a, expected_value, expression)


def _is_greater_than_test_method(a, expected_value):
    contract.is_greater_than(a, expected_value)


def _is_greater_than_or_equal_test_method(a, expected_value):
    contract.is_greater_than_or_equal(a, expected_value)


def _all_have_attribute_test_method(a, expected_attribute_name):
    contract.all_have_attribute(a, expected_attribute_name)


def _all_have_method_test_method(a, expected_method_name):
    contract.all_have_method(a, expected_method_name)


def _is_callable_test_method(a):
    contract.is_callable(a)


def _is_instance_test_method(a, cls):
    contract.is_instance(a, cls)


class _TestClsWithMethodAndAttributes:
    a = 1

    def my_method(self):
        pass
