# -*- coding: utf-8 -*-
from discounts import DiscountsPerFiveItem, DiscountsMoreFiveHundred, NothingDiscounts


class CalculatorDiscounts(object):

    def calc(self, budget):
        discounts = DiscountsMoreFiveHundred(
            DiscountsPerFiveItem(NothingDiscounts())
        ).calc(budget)

        return discounts

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

    print ('Total value of budget %s' % (budget.value))

    calculator = CalculatorDiscounts()
    print ('Discount: %s' % (round(calculator.calc(budget), 2)))

    # Budget Two
    budget = Budget()
    budget.add_item(Item('Product 1', 100))
    budget.add_item(Item('Product 2', 500))
    budget.add_item(Item('Product 3', 400))

    print ('Total value of budget %s' % (budget.value))

    calculator = CalculatorDiscounts()
    print ('Discount: %s' % (round(calculator.calc(budget), 2)))

    # Budget Three
    budget = Budget()
    budget.add_item(Item('Product 1', 10))
    budget.add_item(Item('Product 2', 50))
    budget.add_item(Item('Product 3', 40))

    print ('Total value of budget %s' % (budget.value))

    calculator = CalculatorDiscounts()
    print ('Discount: %s' % (round(calculator.calc(budget), 2)))