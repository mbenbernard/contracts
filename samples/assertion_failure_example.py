# Copyright 2017 Benoit Bernard All Rights Reserved.

from samples.contract_failure_example import build_rocket
from contracts import assertion


if __name__ == "__main__":
    assertion.does_not_raise(ValueError, build_rocket, None)