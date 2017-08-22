# Copyright 2017 Benoit Bernard All Rights Reserved.

from samples.contracts_quick_example import build_rocket
import unittest
from contracts import assertion


class RocketTests(unittest.TestCase):
    def test_build_rocket(self):
        assertion.does_not_raise(ValueError, build_rocket, "Falcon", 9, "SpaceX")