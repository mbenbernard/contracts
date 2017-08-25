# Copyright 2017 Benoit Bernard All Rights Reserved.

from contracts import contract


def contract_is_not_none_demo(a):
    contract.is_not_none(a)

contract_is_not_none_demo("abc")


def contract_is_not_empty_demo(a):
    contract.is_not_empty(a)

contract_is_not_empty_demo("abc")


def contract_is_equal_to_any_demo(a):
    contract.is_equal_to_any(a, [1, 2, 3])

contract_is_equal_to_any_demo(1)


def contract_is_true_demo(a):
    contract.is_true(a)

contract_is_true_demo(2 > 1)


def contract_is_false_demo(a):
    contract.is_false(a)

contract_is_false_demo(1 > 2)


def contract_is_equal_demo(a):
    contract.is_equal(a, 1)

contract_is_equal_demo(1)


def contract_is_greater_than_demo(a):
    contract.is_greater_than(a, 1)

contract_is_greater_than_demo(2)


def contract_is_greater_than_or_equal(a):
    contract.is_greater_than_or_equal(a, 1)

contract_is_greater_than_or_equal(2)


class ClassA:
    abc = 1


class ClassB:
    abc = 1
    xyz = 2


def contract_all_have_attribute(a):
    contract.all_have_attribute(a, "abc")

contract_all_have_attribute([ClassA(), ClassB()])


class ClassC:
    def my_method(self):
        pass


def contract_all_have_method(a):
    contract.all_have_method(a, "my_method")

contract_all_have_method(ClassC())


def contract_is_callable(a):
    contract.is_callable(a)

contract_is_callable(ClassC().my_method)


def contract_is_instance(a):
    contract.is_instance(a, int)

contract_is_instance(1)
