# Copyright 2017 Benoit Bernard All Rights Reserved.

from contracts import contract


def build_rocket(name):
    contract.is_not_empty(name)

    print("You built a {0} rocket".format(name))

if __name__ == "__main__":
    build_rocket(None)