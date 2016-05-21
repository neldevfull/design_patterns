# -*- coding: utf-8 -*-
class ISS(object):

    def calc(self, budget):
        return budget.value * .1

class ICMS(object):

    def calc(self, budget):
        return budget.value * .06
