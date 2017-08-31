"""
code-contracts library
"""

# Make sure that submodules are directly accessible via the top-level 'contracts' module, without having to import
# them explicitly.
from . import contract, assertion

# We use Semantic Versioning. See: http://semver.org/
__title__ = 'code-contracts'
__version__ = '0.1.1'
__build__ = 0x000101
__author__ = 'Benoit Bernard'
__author_email__ = 'aGlAYmVuYmVybmFyZGJsb2cuY29t@base64.email'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2017 Benoit Bernard'
