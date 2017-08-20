import time
import unittest
from contracts import assertion


class RocketTests(unittest.TestCase):
    def test_launch_rocket(self):
        assertion.raises(ValueError, launch_rocket, -1)
        assertion.does_not_raise(ValueError, launch_rocket, 1)


def launch_rocket(delay_in_seconds):
    if delay_in_seconds < 0:
        raise ValueError("delay should be a positive number.")

    time.sleep(delay_in_seconds)

    print("You launched a rocket with a delay of {0} seconds.".format(delay_in_seconds))