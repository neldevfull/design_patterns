# -*- coding: utf-8 -*-
from taxes import ISS, ICMS, ICPP, IKCV


class CalculatorTaxes(object):

    def calculates(self, budget, taxe):
        return taxe.calc(budget)


if __name__ == '__main__':

    from budget import Budget, Item

    # Budget One
    budget = Budget('Budget One')
    budget.add_item(Item('Product 1', 10))
    budget.add_item(Item('Product 2', 5))
    budget.add_item(Item('Product 3', 4))
    budget.add_item(Item('Product 4', 4))
    budget.add_item(Item('Product 5', 4))
    budget.add_item(Item('Product 6', 1))

    # Calculator Taxes
    calculator = CalculatorTaxes()

    print('Budget: %s | Total of items: %s' % (budget.name, budget.total_items))

    print('ISS:  %s' % round(calculator.calculates(budget, ISS()), 2))
    print('ICMS: %s' % round(calculator.calculates(budget, ICMS()), 2))

    print('ISS plus ICMS %s' % round(calculator.calculates(budget, ISS(ICMS())), 2))

    print('ISPP: %s' % round(calculator.calculates(budget, ICPP()), 2))
    print('IKCV: %s' % round(calculator.calculates(budget, IKCV()), 2))

    print('ICPP plus IKCV %s' % round(calculator.calculates(budget, ICPP(IKCV())), 2))