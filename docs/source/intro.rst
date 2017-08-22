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

Why a new library?
------------------

A search for "contract" in Pypi_ leads to many design-by-contract libraries for Python, the most popular being
PyContracts_ and Augment_. These are very good and reasonable choices.

So why create another library?

Well, because I, the author, am not completely satisfied with what exists out there. Many of those libraries:

1. Impose contracts to be written as decorators - which, arguably, might cause them to be viewed as optional and
   not as an essential part of the code.
2. Impose constraints to be written as strings, or as pretty complex lambda expressions - which makes debugging harder,
   and which encourages copy-paste.
3. Raise their own custom exceptions, instead of raising built-in ones like :class:`~ValueError` or :class:`~TypeError`.
4. Mix up the concepts of contract and assertion, while they're normally not intended to be used interchangeably.
5. Have fairly limited documentation, or none at all.
6. Have a fairly limiting license, like some flavor of GPL.
7. Only perform `type checking`_.

Additionally, there were some `early efforts`_ by the Python community to make contracts officially part of the
language, but the idea was apparently abandoned_.

Finally - major spoiler alert - *code-contracts* was essentially made available as an experiment to learn more about
packaging, deploying and documenting `open-source software (OSS)`_.

What about assertions?
----------------------

`Assertions`_ are similar to contracts, in that they impose requirements on your code, but they also differ in some
important ways:

- They're generally used for debugging purposes only.but they're generally used in a different context.

-IMO, contracts and assertions go hand in hand.



It's often assumed that contracts and  play the same role.

Contracts are often used in the form of `preconditions`_ and `postconditions`_, meaning that requirements are either
checked before executing a function or after, respectively. They can also be used in different ways depending on the
library....

and they're often implemented in the
form of `assertions`_.



PEP proposal for contracts: https://www.python.org/dev/peps/pep-0316/



> Explain that it's partly just an exercise/experiment for OSS and documentation.
> So it's not complete. And it doesn't aim to be a full-fledged code contract/assertion library.
> Declarative approach; not an afterthought or optional. This is officially part of the code. Decorators are often used to things that are useful, but optional. I don't like this idea.
> In my opinion, contracts and assertions go hand in hand.
> I coded it well before other contract libraries were made available.

-The idea to to raise a built-in exception whenever a requirement fails.
-Instead of doing "if something: raise ValueError..." you call contract.something(...).
-Should always be enabled. It's similar to raising ValueError yourself.

So far, Python's philosophy has always been to document the behavior of your functions/methods and let them fail
depending on the inputs that they receive. But this approach has proven to be unreliable for projects that reach a
certain size - at least for me. Many corner cases thus go untested. And eventually this causes very bad bugs in
production. Yep, the kind of stuff that **could** be avoided!

This is where code contracts and assertions come to the rescue. There has already been a PEP


#. Beautiful is better than ugly.
#. Explicit is better than implicit.
#. Simple is better than complex.
#. Complex is better than complicated.
#. Readability counts.

All contributions to Requests should keep these important rules in mind.

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

Behavior
--------

Exceptions being raised:

ValueError
TypeError
AssertionError

Features
--------

Provide a table summarizing the available contracts and assertions.

Limitations
-----------

> It's NOT complete.

Apache2 License
---------------

A large number of open source projects you find today are `GPL Licensed`_.
While the GPL has its time and place, it should most certainly not be your
go-to license for your next open source project.

A project that is released as GPL cannot be used in any commercial product
without the product itself also being offered as open source.

The MIT, BSD, ISC, and Apache2 licenses are great alternatives to the GPL
that allow your open-source software to be used freely in proprietary,
closed-source software.

Requests is released under terms of `Apache2 License`_.

.. _`GPL Licensed`: http://www.opensource.org/licenses/gpl-license.php
.. _`Apache2 License`: http://opensource.org/licenses/Apache-2.0


Requests License
----------------

    .. include:: ../../LICENSE