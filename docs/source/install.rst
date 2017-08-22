.. _installation:

Installation
============

These are the installation steps necessary to use *code-contracts* in your projects.

Using pip
---------

Run the following command in your favorite terminal:

.. code-block:: bash

   $ pip install code-contracts

Then you should be able to import the library in your project without any error:

.. code-block:: python

   >>> import contracts

If something went wrong during the installation, importing the library will fail:

.. code-block:: python

   >>> import contracts
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ImportError: No module named 'contracts'

Fortunately, Python 3.4+ already comes shipped with pip_. For earlier versions of Python, you must `install it manually`_.

.. _pip: https://pip.pypa.io/en/stable/
.. _`install it manually`: https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py