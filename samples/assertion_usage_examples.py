# Copyright 2017 Benoit Bernard All Rights Reserved.

from contracts import assertion
from unittest.mock import Mock


assertion.does_not_raise(ValueError, lambda: None)


def raises():
    raise ValueError("Error!")

assertion.raises(ValueError, raises)

assertion.raises_with_msg(ValueError, raises, "Error!")


mock = Mock()
mock.my_method.side_effect = lambda a: a + 1
assertion.not_called_with(mock.my_method, 123)


assertion.contains_one_element_of_class(int, [1])