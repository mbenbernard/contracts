# Copyright 2017 Benoit Bernard All Rights Reserved.

from contracts import contract


def build_rocket(name, model, company):
    contract.is_not_empty(name)
    contract.is_greater_than(model, 0)
    contract.is_not_empty(company)

    print("You built a {0} {1} rocket from {2}.".format(name, model, company))

if __name__ == "__main__":
    build_rocket("Falcon", 9, "SpaceX")