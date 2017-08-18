# Copyright 2017 Benoit Bernard All Rights Reserved.

import unittest
from contracts import assertion
from unittest.mock import Mock


class AssertionTests(unittest.TestCase):
    """
    Class containing unit tests that validate the behavior of assertions.
    """
    def test_does_not_raise(self):
        self._validate(lambda: assertion.does_not_raise(ValueError, _raise, ValueError),
                       "ValueError raised by _raise().")
        self._validate(lambda: assertion.does_not_raise(ValueError, _raise, TypeError))
        self._validate(lambda: assertion.does_not_raise(ValueError, _does_not_raise))

    def test_raises(self):
        self._validate(lambda: assertion.raises(ValueError, _does_not_raise),
                       "ValueError was not raised by _does_not_raise().")
        self._validate(lambda: assertion.raises(ValueError, _raise, TypeError),
                       "ValueError was not raised by _raise().")
        self._validate(lambda: assertion.raises(ValueError, _raise, ValueError))

    def test_raises_with_msg(self):
        self._validate(lambda: assertion.raises_with_msg(ValueError, _does_not_raise, None),
                       "ValueError was not raised by _does_not_raise().")
        self._validate(lambda: assertion.raises_with_msg(ValueError, _raise, "Bad error!", TypeError),
                       "ValueError with message 'Bad error!' was not raised by _raise().")
        self._validate(lambda: assertion.raises_with_msg(ValueError, _raise, "Bad error!", ValueError),
                       "ValueError with message 'Bad error!' was not raised by _raise().")

    def test_not_called_with(self):
        # Method with no call at all.
        mock = Mock()
        mock.non_called_method.return_value = "abc"

        # Method with one basic call.
        mock.called_method_1.return_value = "def"
        mock.called_method_1()

        # Method with two more complex calls, including positional and keyword arguments.
        mock.called_method_2.side_effect = lambda a, b, c: "ghi"
        mock.called_method_2(1, 2, 3)
        mock.called_method_2(4, 5, c=6)
        mock.called_method_2(a=7, c=9, b=8)

        self._validate(lambda: assertion.not_called_with(mock.non_called_method))
        self._validate(lambda: assertion.not_called_with(mock.non_called_method, 1, 2, 3))
        self._validate(lambda: assertion.not_called_with(mock.called_method_1),
                       "Function was unexpectedly called with ().")
        self._validate(lambda: assertion.not_called_with(mock.called_method_2, 1, 2, 3,
                                                         "Function was unexpectedly called with (1, 2, 3)."))
        self._validate(lambda: assertion.not_called_with(mock.called_method_2, 4, 5, c=6),
                       "Function was unexpectedly called with (4, 5, c=6).")
        self._validate(lambda: assertion.not_called_with(mock.called_method_2, a=7, b=8, c=9),
                       "Function was unexpectedly called with (a=7, b=8, c=9).")

    def test_contains_one_element_of_class(self):
        self._validate(lambda: assertion.contains_one_element_of_class(int, []),
                       "Iterable should contain one and only one object of class 'int'.")
        self._validate(lambda: assertion.contains_one_element_of_class(int, ["dummy"]),
                       "Iterable should contain one and only one object of class 'int'.")
        self._validate(lambda: assertion.contains_one_element_of_class(int, [1, 2]),
                       "Iterable should contain one and only one object of class 'int'.")
        self._validate(lambda: assertion.contains_one_element_of_class(int, [1]))

    def _validate(self, callable_assertion, expected_assertion_msg=None):
        # To validate results, we use the assertions found in the :class:`~unittest.TestCase` class.
        try:
            callable_assertion()
            if expected_assertion_msg:
                # If we're here, it means that the assertion should have raised, but it didn't.
                self.fail("The assertion should have raised!")
        except Exception as e:
            if expected_assertion_msg:
                self.assertIsInstance(e, AssertionError)
                self.assertEqual(str(e), expected_assertion_msg)
            else:
                self.fail("The assertion should not have raised!")


def _raise(exception_cls, exception_msg=None):
    raise exception_cls(exception_msg)


def _does_not_raise():
    pass
