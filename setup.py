# Copyright 2017 Benoit Bernard All Rights Reserved.

import contracts
from setuptools import setup

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(name=contracts.__title__,
      version=contracts.__version__,
      description='A library that provides code contracts and assertions.',
      long_description=readme,
      url='https://github.com/mbenbernard/contracts',
      author=contracts.__author__,
      author_email='',
      license=contracts.__license__,
      packages=['contracts'],
      zip_safe=False,
      python_requires='>=3',
      install_requires=[],
      classifiers=(
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy'
      ))
