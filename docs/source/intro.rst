.. _introduction:

Introduction
============

Philosophy and purpose
----------------------

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

.. _`apache2`:

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