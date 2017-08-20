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
is expected from your code before it executes, so that you avoid costly errors and bugs.

Here's a quick example demonstrating the use of contracts:

.. literalinclude:: ../../samples/contracts_quick_example.py
   :language: python
   :linenos:

And here's an example of assertions used in the context of unit tests:

.. literalinclude:: ../../samples/assertions_quick_example.py
   :language: python
   :linenos:

**code-contracts** officially supports Python 3.0 and onwards.

The User Guide
--------------

.. toctree::
    :maxdepth: 2

    intro
    install
    examples

The API Documentation / Guide
-----------------------------

.. toctree::
    :maxdepth: 2

    api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
