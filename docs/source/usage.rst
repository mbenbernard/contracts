.. _usage:

Usage
=====

Importing the right module
--------------------------

*code-contracts* is split into two different modules: contract_ and assertion_.

To use contracts, just import the following module:

.. code-block:: python

   >>> from contracts import contract

To use assertions, import the following module:

.. code-block:: python

   >>> from contracts import assertion

Expected behavior
-----------------

When a contract or an assertion fails, you can expect it to raise an exception as follows:

+----------------------------+-----------------------------------------+
| Entity                     | Exception(s) raised                     |
+============================+=========================================+
| :mod:`~contracts.contract` | :class:`TypeError`, :class:`ValueError` |
+----------------------------+-----------------------------------------+
| :mod:`~contracts.assertion`| :class:`AssertionError`                 |
+----------------------------+-----------------------------------------+

The contracts provided can be used as either `preconditions`_ or `postconditions`_, meaning that requirements can be
checked either before executing a function or after, respectively.

Contracts' behavior
^^^^^^^^^^^^^^^^^^^

Here's a concrete example of what happens when a contract fails:

.. literalinclude:: ../../samples/contract_failure_example.py
   :language: python
   :linenos:
   :lines: 3-

.. code-block:: python

    Traceback (most recent call last):
      File "/contracts/samples/contract_failure_example.py", line 14, in <module>
        build_rocket(None, 9, "SpaceX")
      File "/contracts/samples/contract_failure_example.py", line 7, in build_rocket
        contract.is_not_empty(name)
      File /contracts/contracts/contract.py", line 37, in is_not_empty
        raise ValueError("{0} was empty.".format(_get_parameter_name()))
    ValueError: name was empty.

So when you run this script, the contract raises a :class:`ValueError` indicating that the `name` parameter is empty.
Typically, you want this error to bubble up and crash your program as demonstrated. This way, you can more easily
track the error and fix the calling code accordingly.

Assertions' behavior
^^^^^^^^^^^^^^^^^^^^

Now, here's a concrete example of what happens when an assertion fails:

.. literalinclude:: ../../samples/assertion_failure_example.py
   :language: python
   :linenos:
   :lines: 4-

.. code-block:: python

    Traceback (most recent call last):
      File "/contracts/contracts/assertion.py", line 21, in does_not_raise
        callable_obj(*args, **kwargs)
      File "/contracts/samples/contract_failure_example.py", line 7, in build_rocket
        contract.is_not_empty(name)
      File "/contracts/contracts/contract.py", line 37, in is_not_empty
        raise ValueError("{0} was empty.".format(_get_parameter_name()))
    ValueError: name was empty.

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "/contracts/samples/assertion_failure_example.py", line 8, in <module>
        assertion.does_not_raise(ValueError, build_rocket, None)
      File "/contracts/contracts/assertion.py", line 25, in does_not_raise
        raise AssertionError("{0} raised by {1}().".format(exception_cls.__name__, callable_obj.__name__))
    AssertionError: ValueError raised by build_rocket().

So when you run this script, the assertion raises an :class:`AssertionError` indicating that
:func:`~samples.contract_failure_example.build_rocket` itself raises a :class:`ValueError`. Again, this is because the
`name` parameter is empty.

As you can see, assertions are very handy to validate the expected behavior of a function or method. Note that it's a
bit more common to use assertions in the context of more formal unit tests, like when using the :mod:`~unittest` module,
as it handles :class:`AssertionError` a little bit more gracefully.

Available contracts and assertions
----------------------------------

-Features/available asserts + contracts in a table

Concrete examples
-----------------

-For each contract function
-For each assertion function


.. _contract: abc
.. _assertion: abc
.. _preconditions: https://en.wikipedia.org/wiki/Precondition
.. _postconditions: https://en.wikipedia.org/wiki/Postcondition