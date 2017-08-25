.. _usage:

Usage
=====

Importing the right module
--------------------------

*code-contracts* is split into two different modules: :mod:`~contracts.contract` and :mod:`~contracts.assertion`.

To use contracts, just import the following module:

.. code-block:: python

   >>> from contracts import contract

To use assertions, import the following module:

.. code-block:: python

   >>> from contracts import assertion

Expected behavior
-----------------

When a contract or an assertion fails, you can expect it to raise an exception as follows:

+----------------------------+--------------------------------------------------------------------+
| Entity                     | Exception(s) raised                                                |
+============================+====================================================================+
| :mod:`~contracts.contract` | :class:`TypeError`, :class:`ValueError` or :class:`AttributeError` |
+----------------------------+--------------------------------------------------------------------+
| :mod:`~contracts.assertion`| :class:`AssertionError`                                            |
+----------------------------+--------------------------------------------------------------------+

The contracts provided are intended to be used as `preconditions`_, meaning that requirements will be checked before
executing a function.

Contracts' behavior
^^^^^^^^^^^^^^^^^^^

Here's what happens when a contract fails:

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

Here's what happens when an assertion fails:

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

Available contracts
-------------------

*code-contracts* contains the following contract functions:

+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Function                                             | Description                                                                                                                                        | Example                                                      |
+======================================================+====================================================================================================================================================+==============================================================+
| :func:`~contracts.contract.is_not_none`              | Checks that the specified value is not equal to None.                                                                                              | .. literalinclude:: ../../samples/contract_usage_examples.py |
|                                                      |                                                                                                                                                    |    :language: python                                         |
|                                                      |                                                                                                                                                    |    :lines: 6-9                                               |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| :func:`~contracts.contract.is_not_empty`             | Checks that the specified value is not empty.                                                                                                      | .. literalinclude:: ../../samples/contract_usage_examples.py |
|                                                      |                                                                                                                                                    |    :language: python                                         |
|                                                      |                                                                                                                                                    |    :lines: 12-15                                             |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| :func:`~contracts.contract.is_equal_to_any`          | Checks that the specified value is equal to at least one of the expected values.                                                                   | .. literalinclude:: ../../samples/contract_usage_examples.py |
|                                                      |                                                                                                                                                    |    :language: python                                         |
|                                                      |                                                                                                                                                    |    :lines: 18-21                                             |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| :func:`~contracts.contract.is_true`                  | Checks that the specified value is equal to True.                                                                                                  | .. literalinclude:: ../../samples/contract_usage_examples.py |
|                                                      |                                                                                                                                                    |    :language: python                                         |
|                                                      |                                                                                                                                                    |    :lines: 24-27                                             |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| :func:`~contracts.contract.is_false`                 | Checks that the specified value is equal to False.                                                                                                 | .. literalinclude:: ../../samples/contract_usage_examples.py |
|                                                      |                                                                                                                                                    |    :language: python                                         |
|                                                      |                                                                                                                                                    |    :lines: 30-33                                             |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| :func:`~contracts.contract.is_equal`                 | Checks that the specified value is strictly equal to the expected value.                                                                           | .. literalinclude:: ../../samples/contract_usage_examples.py |
|                                                      |                                                                                                                                                    |    :language: python                                         |
|                                                      |                                                                                                                                                    |    :lines: 36-39                                             |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| :func:`~contracts.contract.is_greater_than`          | Checks that the specified value is greater than the expected value.                                                                                | .. literalinclude:: ../../samples/contract_usage_examples.py |
|                                                      |                                                                                                                                                    |    :language: python                                         |
|                                                      |                                                                                                                                                    |    :lines: 42-45                                             |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| :func:`~contracts.contract.is_greater_than_or_equal` | Checks that the specified value is greater than or strictly equal to the expected value.                                                           | .. literalinclude:: ../../samples/contract_usage_examples.py |
|                                                      |                                                                                                                                                    |    :language: python                                         |
|                                                      |                                                                                                                                                    |    :lines: 48-51                                             |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| :func:`~contracts.contract.all_have_attribute`       | Checks that all objects contained in value - be it a single object or an :class:`~collections.Iterable` of objects - have the specified attribute. | .. literalinclude:: ../../samples/contract_usage_examples.py |
|                                                      |                                                                                                                                                    |    :language: python                                         |
|                                                      |                                                                                                                                                    |    :lines: 54-66                                             |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| :func:`~contracts.contract.all_have_method`          | Checks that all objects contained in value - be it a single object or an :class:`~collections.Iterable` of objects have the specified method.      | .. literalinclude:: ../../samples/contract_usage_examples.py |
|                                                      |                                                                                                                                                    |    :language: python                                         |
|                                                      |                                                                                                                                                    |    :lines: 69-77                                             |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| :func:`~contracts.contract.is_callable`              | Checks that the specified value is a callable object (i.e. has a '__call__' attribute).                                                            | .. literalinclude:: ../../samples/contract_usage_examples.py |
|                                                      |                                                                                                                                                    |    :language: python                                         |
|                                                      |                                                                                                                                                    |    :lines: 80-83                                             |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| :func:`~contracts.contract.is_instance`              | Checks that the specified value is an instance of the given class.                                                                                 | .. literalinclude:: ../../samples/contract_usage_examples.py |
|                                                      |                                                                                                                                                    |    :language: python                                         |
|                                                      |                                                                                                                                                    |    :lines: 86-89                                             |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

.. note::

   Some of these contract functions contain an optional parameter named `expression_str`. Its purpose is to allow you
   to pass a string representation of the value passed to the function. This is especially useful if, for example,
   the value isn't a single, discrete value, but a boolean expression such as x > y. In such a case, you can pass
   'x > y' in `expression_str`. This expression will be used to create a more meaningful error message if the contract
   fails.

Available assertions
--------------------

*code-contracts* contains the following assertion functions:

+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| Function                                                   | Description                                                                                                                  | Example                                                       |
+============================================================+==============================================================================================================================+===============================================================+
| :func:`~contracts.assertion.does_not_raise`                | Asserts that the specified callable object does not raise an exception of the specified class when called.                   | .. literalinclude:: ../../samples/assertion_usage_examples.py |
|                                                            |                                                                                                                              |    :language: python                                          |
|                                                            |                                                                                                                              |    :lines: 7                                                  |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| :func:`~contracts.assertion.raises`                        | Asserts that the specified callable object raises an exception of the specified class when called.                           | .. literalinclude:: ../../samples/assertion_usage_examples.py |
|                                                            |                                                                                                                              |    :language: python                                          |
|                                                            |                                                                                                                              |    :lines: 10-13                                              |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| :func:`~contracts.assertion.raises_with_msg`               | Asserts that the specified callable object raises an exception of the specified type with the specified message when called. | .. literalinclude:: ../../samples/assertion_usage_examples.py |
|                                                            |                                                                                                                              |    :language: python                                          |
|                                                            |                                                                                                                              |    :lines: 10-11, 14-15                                       |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| :func:`~contracts.assertion.not_called_with`               | Asserts that the specified mock object was never called with a specific sequence of arguments.                               | .. literalinclude:: ../../samples/assertion_usage_examples.py |
|                                                            |                                                                                                                              |    :language: python                                          |
|                                                            |                                                                                                                              |    :lines: 18-20                                              |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| :func:`~contracts.assertion.contains_one_element_of_class` | Asserts that the specified iterable object contains one and only one element of the specified class.                         | .. literalinclude:: ../../samples/assertion_usage_examples.py |
|                                                            |                                                                                                                              |    :language: python                                          |
|                                                            |                                                                                                                              |    :lines: 23                                                 |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

.. _preconditions: https://en.wikipedia.org/wiki/Precondition