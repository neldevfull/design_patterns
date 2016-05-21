# -*- coding: utf-8 -*-
class DiscountsPerFiveItem(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calc(self, budget):
        if budget.total_items > 5:
            return budget.value * .1
        else:
            return self.__next_discount.calc(budget)


class DiscountsMoreFiveHundred(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calc(self, budget):
        if budget.value > 500:
            return budget.value * .07
        else:
            return self.__next_discount.calc(budget)


class NothingDiscounts(object):

    def calc(self, budget):
        return 0