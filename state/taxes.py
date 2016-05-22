# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Taxes(object):

    def __init__(self, other_taxes = None):
        self.__other_taxes = other_taxes

    def calc_other_taxes(self, budget):
        if self.__other_taxes is None:
            return 0

        return self.__other_taxes.calc(budget)

    @abstractmethod
    def calc(self, budget):
        pass


# Abstract Class
class TemplateTaxes(Taxes):

    # Magic attribute
    __metaclass__ = ABCMeta

    def calc(self, budget):
        if self.condition_max_taxes(budget):
            return self.max_taxes(budget) + self.calc_other_taxes(budget)
        else:
            return self.min_taxes(budget) + self.calc_other_taxes(budget)

    @abstractmethod
    def condition_max_taxes(self, budget):
        pass

    @abstractmethod
    def max_taxes(self, budget):
        pass

    @abstractmethod
    def min_taxes(self, budget):
        pass


# Method for making decorator
def IPVX(method):
    def wrapper(self, budget):
        return method(self, budget) + 50.00

    return wrapper


class ISS(Taxes):

    @IPVX
    def calc(self, budget):
        return budget.value * .1 + self.calc_other_taxes(budget)


class ICMS(Taxes):

    def calc(self, budget):
        return budget.value * .06 + self.calc_other_taxes(budget)


class ICPP(TemplateTaxes):

    def condition_max_taxes(self, budget):
        return budget.value > 500

    def max_taxes(self, budget):
        return budget.value * .07

    def min_taxes(self, budget):
        return budget.value * .05


class IKCV(TemplateTaxes):

    def condition_max_taxes(self, budget):
        return budget.value > 500 and self.__item_greater_hundred(budget)

    def max_taxes(self, budget):
        return budget.value * .1

    def min_taxes(self, budget):
        return budget.value *.06

    def __item_more_hundred(self, budget):
        for item in budget.get_items:
            if item.value > 100:
                return True
        return False
