code-contracts: Contracts and Assertions for Python
===================================================

**code-contracts** is a library that provides:

1. **Contracts**
    Functions that impose requirements when entering a function or method - also commonly called *preconditions*.
2. **Assertions**
    Functions that impose requirements in the body of a function or method. This is not a complete suite of assertions;
    instead, they are meant to be complementary to those available in `unittest.TestCase`.

The goal of this library is not to make Python a statically-typed language. Instead, it aims to help you define what
is expected from your code before it executes, so that you can more easily track and prevent bugs.

So here's how you can use contracts:

.. code-block:: python

    from contracts import contract


    def build_rocket(name, model, company):
        contract.is_not_empty(name)
        contract.is_greater_than(model, 0)
        contract.is_not_empty(company)

        print("You built a {0} {1} rocket from {2}.".format(name, model, company))

    if __name__ == "__main__":
        build_rocket("Falcon", 9, "SpaceX")

And here's how you can use assertions to unit test the above function:

.. code-block:: python

    import unittest
    from contracts import assertion


    class RocketTests(unittest.TestCase):
        def test_build_rocket(self):
            assertion.does_not_raise(ValueError, build_rocket, "Falcon", 9, "SpaceX")

**code-contracts** officially supports Python 3.3 and onwards.

Installation
------------

Simply run the following command in your favorite terminal:

.. code-block:: bash

   $ pip install code-contracts

Documentation
-------------

The full documentation is available at http://contracts.readthedocs.io/.