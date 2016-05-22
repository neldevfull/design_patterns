# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


# Magic attribute
class Status(object):
    # Magic attribute
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply_discount_extra(self, budget):
        pass

    @abstractmethod
    def approves(self, budget):
        pass

    @abstractmethod
    def disapproves(self, budget):
        pass

    @abstractmethod
    def finalizes(self, budget):
        pass


class InApproval(Status):
    def apply_discount_extra(self, budget):
        budget.add_discounts_extra(budget.value * .02)

    def approves(self, budget):
        budget.status = Approved()

    def disapproves(self, budget):
        budget.status = Disapproved()

    def finalizes(self, budget):
        raise Exception('Budget in approval can not go finalizes')


class Approved(Status):
    def apply_discount_extra(self, budget):
        budget.add_discounts_extra(budget.value * .05)

    def approves(self, budget):
        raise Exception('Approved budget cannot be approved again')

    def disapproves(self, budget):
        raise Exception('Approved budget cannot be disapproved')

    def finalizes(self, budget):
        budget.status = Finalized()


class Disapproved(Status):
    def apply_discount_extra(self, budget):
        raise Exception('Budget disapproved.You do not receive extra discount')

    def approves(self, budget):
        raise Exception('Disapproved budget cannot be approved')

    def disapproves(self, budget):
        raise Exception('Disapproved budget cannot be disapproved again')

    def finalizes(self, budget):
        budget.status = Finalized()


class Finalized(Status):
    def apply_discount_extra(self, budget):
        raise Exception('Budget finalized.You do not receive extra discount')

    def approves(self, budget):
        raise Exception('Budget already finalized!')

    def disapproves(self, budget):
        raise Exception('Budget already finalized!')

    def finalizes(self, budget):
        raise Exception('Budget already finalized!')


class Budget(object):

    def __init__(self, name):
        self.__name           = name
        self.__items          = []
        self.status           = InApproval()
        self.__discount_extra = 0

    def approves(self):
        self.status.approves(budget)

    def disapproves(self):
        self.status.disapproves(budget)

    def finalizes(self):
        pass

    def apply_discount_extra(self):
        self.status.apply_discount_extra(self)

    def add_discounts_extra(self, discount):
        self.__discount_extra += discount

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

# -- Test ---
if __name__ == '__main__':
    # Budget Owner
    budget = Budget('Budget One')
    budget.add_item(Item('Product 1', 10))
    budget.add_item(Item('Product 2', 5))
    budget.add_item(Item('Product 3', 4))
    budget.add_item(Item('Product 4', 4))
    budget.add_item(Item('Product 5', 4))
    budget.add_item(Item('Product 6', 1))

    print(budget.value)

    budget.approves()
    budget.apply_discount_extra()
    print(budget.value)

    budget.finalizes()
    budget.apply_discount_extra()
    print(budget.value)