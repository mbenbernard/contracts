.. _introduction:

Introduction
============

What's a contract?
------------------

Design-by-contract_ programming is an approach by which you define the requirements or expectations of your code
before it executes. So when some external code calls your own code, it's expected that the former meets the requirements
of the latter. In other words, it must respect the established *contract*. Otherwise, an error is raised.

So let's say that you have the following function:

.. literalinclude:: ../../samples/contracts_vs_manual_checks_example.py
   :language: python
   :linenos:
   :lines: 8-9
   :dedent: 4

You'd normally do what follows to impose requirements on its parameters:

.. literalinclude:: ../../samples/contracts_vs_manual_checks_example.py
   :language: python
   :linenos:
   :lines: 14-22
   :dedent: 4

So any time one of those requirements isn't met, it raises a :class:`~ValueError`.

Now, this may be quite handy to prevent potential bugs. And this may work quite well for a single script that contains
only a few functions. But:

- Do you see yourself repeating those manual checks everywhere in a much larger program?
- What if you'd like those checks to cover a little bit more ground, like supporting more data types or performing
  more complex validations?

Then you'd most likely need to create a collection of well-tested contracts, so that you can reuse them whenever needed.
Enters the *code-contracts* library!

Here's how using contracts greatly simplifies the previous example:

.. literalinclude:: ../../samples/contracts_vs_manual_checks_example.py
   :language: python
   :linenos:
   :lines: 27-32
   :dedent: 4

Why a new library?
------------------

A search for "contract" in Pypi_ leads to many design-by-contract libraries for Python, the most popular being
PyContracts_ and Augment_. These are very good and reasonable choices.

So why create another library?

Well, because I, the author, am not completely satisfied with what exists out there. Many of those libraries:

1. Impose contracts to be written as decorators - which, arguably, might lead people to view them as optional or as an
   afterthought, while they're really an essential part of your code.
2. Impose constraints to be written as strings, or as pretty complex lambda expressions - which makes debugging harder,
   and which encourages copy-paste.
3. Raise their own custom exceptions, instead of raising built-in ones like :class:`~ValueError` or :class:`~TypeError`.
4. Mix up the concepts of contract and assertion, while they're normally not intended to be used interchangeably.
5. Have fairly limited documentation, or none at all.
6. Have a fairly limiting license, like some flavor of GPL_.
7. Only perform `type checking`_.

Additionally, there were some `early efforts`_ by the Python community to make contracts officially part of the
language, but the idea was apparently abandoned_.

Finally - major spoiler alert - *code-contracts* is above all else an experiment to learn more about packaging,
deploying and documenting `open-source software (OSS)`_.

What about assertions?
----------------------

`Assertions`_ are similar to contracts, in that they impose requirements on your code. But they also differ in some
important ways:

- They're generally used for debugging purposes only.
- They're often used in unit tests to validate results.

So assertions and contracts are definitely complementary to each other.

Python already provides many assertions in the :class:`~unittest.TestCase` class, but a few important ones are missing.
For example, you can validate that a function raises an error using :meth:`~unittest.TestCase.assertRaises`, but
there's nothing like `assertNotRaises` or anything equivalent, surprisingly.

This is why *code-contracts* provides a few of those useful, but missing assertions, in addition to contracts.

Here's an example using :func:`~contracts.assertion.does_not_raise`:

.. literalinclude:: ../../samples/assertions_quick_example.py
   :language: python
   :linenos:
   :lines: 4-

Expected behavior
-----------------

When a contract or an assertion fails, you can expect it to raise an exception as follows:

+----------------------------+-----------------------------------------+
| Module                     | Exception(s) raised                     |
+============================+=========================================+
| :mod:`~contracts.contract` | :class:`TypeError`, :class:`ValueError` |
+----------------------------+-----------------------------------------+
| :mod:`~contracts.assertion`| :class:`AssertionError`                 |
+----------------------------+-----------------------------------------+

The contracts provided can be used as either `preconditions`_ or `postconditions`_, meaning that requirements can be
checked either before executing a function or after, respectively.

Limitations
-----------

*code-contracts* has been battle-tested via unit testing and heavy use across several projects, so it's fairly stable.

But don't expect it to be a full-fledged library; it only provides a few functions to fill the gaps of existing
libraries.

Also, remember that *code-contracts* is essentially an experiment with OSS, as stated previously. Feel free to submit
bug reports and feature requests, though.

License
-------

*code-contracts* is released under the terms of the `Apache License Version 2.0`_:

    .. include:: ../../LICENSE

The current documentation is released under the terms of the `Creative Commons Attribution-ShareAlike 4.0 International License`_.

.. _Pypi: https://pypi.python.org/pypi
.. _design-by-contract: https://en.wikipedia.org/wiki/Design_by_contract
.. _preconditions: https://en.wikipedia.org/wiki/Precondition
.. _postconditions: https://en.wikipedia.org/wiki/Postcondition
.. _Assertions: https://en.wikipedia.org/wiki/Assertion_(software_development)
.. _PyContracts: https://pypi.python.org/pypi/PyContracts/
.. _Augment: https://pypi.python.org/pypi/Augment/
.. _type checking: https://en.wikipedia.org/wiki/Type_system#Type_checking
.. _`early efforts`: https://www.python.org/dev/peps/pep-0316/
.. _abandoned: https://mail.python.org/pipermail/python-list/2007-August/436816.html
.. _`open-source software (OSS)`: https://en.wikipedia.org/wiki/Open-source_software
.. _GPL: https://www.gnu.org/licenses/gpl-3.0.en.html
.. _`Apache License Version 2.0`: https://www.apache.org/licenses/LICENSE-2.0
.. _`Creative Commons Attribution-ShareAlike 4.0 International License`: https://creativecommons.org/licenses/by-sa/4.0/
