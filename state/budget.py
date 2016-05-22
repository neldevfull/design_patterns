# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


# Magic attribute
class Status(object):
    # Magic attribute
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply_discount_extra(self, budget):
        pass


class InApproval(Status):
    def apply_discount_extra(self, budget):
        budget.add_discounts_extra(budget.value * .02)


class Approved(Status):
    def apply_discount_extra(self, budget):
        budget.add_discounts_extra(budget.value * .05)


class Disaproved(Status):
    def apply_discount_extra(self, budget):
        raise Exception('Budget disapproved.You do not receive extra discount')


class Finalized(Status):
    def apply_discount_extra(self, budget):
        raise Exception('Budget finalized.You do not receive extra discount')


class Budget(object):

    def __init__(self, name):
        self.__name           = name
        self.__items          = []
        self.status           = InApproval()
        self.__discount_extra = 0

    def apply_discounts_extra(self, discount):
        self.status.apply_discount_extra(self)

    def add_discounts_extra(self, discount):
        return self.__discount_extra += discount

    @property
    def value(self):
        total = 0.0
        for item in self.__items:
            total += item.value
        return total - self.__discount_extra

    def get_items(self):
        return tuple(self.__items)

    @property
    def total_items(self):
        return len(self.__items)

    def add_item(self, item):
        self.__items.append(item)

    @property
    def name(self):
        return self.__name


class Item(object):

    def __init__(self, name, value):
        self.__name  = name
        self.__value = value

    @property
    def value(self):
        return self.__value

    @property
    def name(self):
        return self.__name
