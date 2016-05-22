# -*- coding: utf-8 -*-
from taxes import ISS, ICMS, ICPP, IKCV


class CalculatorTaxes(object):

    def calculates(self, budget, taxe):

        print(round(taxe.calc(budget), 2))


if __name__ == '__main__':

    from budget import Budget, Item

    # Budget One
    budget = Budget()
    budget.add_item(Item('Product 1', 10))
    budget.add_item(Item('Product 2', 5))
    budget.add_item(Item('Product 3', 4))
    budget.add_item(Item('Product 4', 4))
    budget.add_item(Item('Product 5', 4))
    budget.add_item(Item('Product 6', 1))

    # Calculator Taxes
    calculator = CalculatorTaxes()

    print('ISS and ICMS')
    calculator.calculates(budget, ISS())
    calculator.calculates(budget, ICMS())

    print('ISPP and IKCV')
    calculator.calculates(budget, ICPP())
    calculator.calculates(budget, IKCV())