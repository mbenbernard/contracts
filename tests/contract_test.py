# Copyright 2017 Benoit Bernard All Rights Reserved.

import unittest
from contracts import assertion
from contracts import contract


class ContractsTests(unittest.TestCase):
    """
    Class containing unit tests that validate the behavior of code contracts for module-level functions.
    """
    def test_is_not_none_asserts(self):
        assertion.raises_with_msg(TypeError, _is_not_none_test_method, "a was equal to None.", None)

    def test_is_not_none_does_not_assert(self):
        assertion.does_not_raise(TypeError, _is_not_none_test_method, "123")

    def test_is_not_empty_asserts(self):
        assertion.raises_with_msg(ValueError, _is_not_empty_test_method, "a was empty.", None)
        assertion.raises_with_msg(ValueError, _is_not_empty_test_method, "a was empty.", "")
        assertion.raises_with_msg(ValueError, _is_not_empty_test_method, "a was empty.", [])

    def test_is_not_empty_does_not_assert(self):
        assertion.does_not_raise(TypeError, _is_not_empty_test_method, "123")
        assertion.does_not_raise(TypeError, _is_not_empty_test_method, [123])

    def test_is_of_type_asserts(self):
        assertion.raises_with_msg(TypeError, _is_of_type_test_method, "a was of type int while the expected type was str.", 1, str)

    def test_is_of_type_does_not_assert(self):
        assertion.does_not_raise(TypeError, _is_of_type_test_method, "abc", str)

    def test_is_equal_to_any_asserts(self):
        assertion.raises_with_msg(ValueError, _is_equal_to_any_test_method, "a with value 4 and type int was not equal to any of the expected values.", 4, [1, 2, 3])
        assertion.raises_with_msg(ValueError, _is_equal_to_any_test_method, "something.abc with value 4 and type int was not equal to any of the expected values.", 4, [1, 2, 3], "something.abc")

    def test_is_equal_to_any_does_not_assert(self):
        assertion.does_not_raise(ValueError, _is_equal_to_any_test_method, 1, [1, 2, 3])

    def test_is_true_asserts(self):
        assertion.raises_with_msg(ValueError, _is_true_test_method, "a > 0 was not True.", -1, "a > 0")

    def test_is_true_does_not_assert(self):
        assertion.does_not_raise(ValueError, _is_true_test_method, 1)

    def test_is_false_asserts(self):
        assertion.raises_with_msg(ValueError, _is_false_test_method, "a > 0 was not False.", 1, "a > 0")

    def test_is_false_does_not_assert(self):
        assertion.does_not_raise(ValueError, _is_false_test_method, -1)

    def test_is_equal_asserts(self):
        assertion.raises_with_msg(ValueError, _is_equal_test_method, "a with value 2 was not equal to 1.", 2, 1)
        assertion.raises_with_msg(ValueError, _is_equal_test_method, "self.a with value 2 was not equal to 1.", 2, 1, "self.a")
        assertion.raises_with_msg(ValueError, _is_equal_test_method, "len(tuple) with value 2 was not equal to 1.", len((1, 2)), 1, "len(tuple)")

    def test_is_equal_does_not_assert(self):
        assertion.does_not_raise(ValueError, _is_equal_test_method, 1, 1)
        assertion.does_not_raise(ValueError, _is_equal_test_method, "", "")

    def test_is_greater_than_asserts(self):
        assertion.raises_with_msg(ValueError, _is_greater_than_test_method, "a with value 1 was not greater than 2.", 1, 2)

    def test_is_greater_than_does_not_assert(self):
        assertion.does_not_raise(ValueError, _is_greater_than_test_method, 2, 1)

    def test_is_not_none_on_xth_parameter_asserts(self):
        assertion.raises_with_msg(TypeError, _is_not_none_on_xth_parameter_test_method, "a was equal to None.", None, "def", "ghi")
        assertion.raises_with_msg(TypeError, _is_not_none_on_xth_parameter_test_method, "b was equal to None.", "abc", None, "ghi")
        assertion.raises_with_msg(TypeError, _is_not_none_on_xth_parameter_test_method, "c was equal to None.", "abc", "def", None)

    def test_is_instance_success(self):
        try:
            self._is_instance_test_method(True, bool)
            success = True
        except TypeError:
            success = False
        self.assertTrue(success)

    def test_is_instance_failure(self):
        try:
            self._is_instance_test_method(True, str)
            success = False
        except TypeError as e:
            self.assertEqual(str(e), "value was not an instance of str.")
            success = True
        self.assertTrue(success)

    def _is_instance_test_method(self, value, cls):
        contract.is_instance(value, cls)


class TestClsTests(unittest.TestCase):
    """
    Class containing unit tests that validate the behavior of code contracts for class-level functions (methods).
    """
    def test_one_method(self):
        test = _TestCls(None)
        assertion.raises(TypeError, test.one_method)


def _is_not_none_test_method(a):
    contract.is_not_none(a)


def _is_not_empty_test_method(a):
    contract.is_not_empty(a)


def _is_of_type_test_method(a, expected_type):
    contract.is_of_type(a, expected_type)


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


def _is_not_none_on_xth_parameter_test_method(a, b, c):
    contract.is_not_none(a)
    contract.is_not_none(b)
    contract.is_not_none(c)


class _TestCls:
    def __init__(self, the_param):
        self.the_param = the_param

    def one_method(self):
        contract.is_not_none(self.the_param)