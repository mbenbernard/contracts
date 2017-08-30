.. code-contracts documentation master file, created by
   sphinx-quickstart on Fri Mar 24 16:02:10 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

code-contracts: Contracts and Assertions for Python
===================================================

Release v\ |version|. (:ref:`Installation <install>`)

**code-contracts** is a library that provides:

1. **Contracts**
    Functions that impose requirements when entering a function or method - also commonly called *preconditions*.
2. **Assertions**
    Functions that impose requirements in the body of a function or method. This is not a complete suite of assertions;
    instead, they are meant to be complementary to those available in :class:`~unittest.TestCase`.

The goal of this library is not to make Python a statically-typed language. Instead, it aims to help you define what
is expected from your code before it executes, so that you can more easily track and prevent bugs.

So here's how you can use contracts:

.. literalinclude:: ../../samples/contracts_quick_example.py
   :language: python
   :linenos:
   :lines: 3-

And here's how you can use assertions to unit test the above function:

.. literalinclude:: ../../samples/assertions_quick_example.py
   :language: python
   :linenos:
   :lines: 4-

**code-contracts** officially supports Python 3.3 and onwards.

The User Guide
--------------

.. toctree::
    :maxdepth: 2

    intro
    install
    usage

The API Documentation / Guide
-----------------------------

.. toctree::
    :maxdepth: 2

    api
