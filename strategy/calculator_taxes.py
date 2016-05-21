# -*- coding: utf-8 -*-
from taxes import ISS, ICMS


class CalculatorTaxes(object):

    def calculates(self, budget, taxe):

        print(taxe.calc(budget))


if __name__ == '__main__':
    from budget import Budget

    calculator = CalculatorTaxes()
    budget     = Budget(500)

    calculator.calculates(budget, ISS())
    calculator.calculates(budget, ICMS())
