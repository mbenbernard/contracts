# Copyright 2017 Benoit Bernard All Rights Reserved.

from contracts import contract


class RocketVanilla:
    @staticmethod
    def build_rocket(name, model, company):
        print("You built a {0} {1} rocket from {2}.".format(name, model, company))


class RocketWithManualChecks:
    @staticmethod
    def build_rocket(name, model, company):
        if not name:
            raise ValueError("name should not be empty")
        if model <= 0:
            raise ValueError("model should be greater than 0")
        if not company:
            raise ValueError("company should not be empty")

        print("You built a {0} {1} rocket from {2}.".format(name, model, company))


class RocketWithContracts:
    @staticmethod
    def build_rocket(name, model, company):
        contract.is_not_empty(name)
        contract.is_greater_than(model, 0)
        contract.is_not_empty(company)

        print("You built a {0} {1} rocket from {2}.".format(name, model, company))


if __name__ == "__main__":
    RocketVanilla.build_rocket("Falcon", 9, "SpaceX")
    RocketWithManualChecks.build_rocket("Falcon", 9, "SpaceX")
    RocketWithContracts.build_rocket("Falcon", 9, "SpaceX")
