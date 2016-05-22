# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


# Abstract Class
class TemplateTaxes(object):

    # Magic attribute
    __metaclass__ = ABCMeta

    def calc(self, budget):
        if self.condition_max_taxes(budget):
            return self.max_taxes(budget)
        else:
            return self.min_taxes(budget)

    @abstractmethod
    def condition_max_taxes(self, budget):
        pass

    @abstractmethod
    def max_taxes(self, budget):
        pass

    @abstractmethod
    def min_taxes(self, budget):
        pass


class ISS(object):

    def calc(self, budget):
        return budget.value * .1


class ICMS(object):

    def calc(self, budget):
        return budget.value * .06


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
