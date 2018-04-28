#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import inf, exp, log
NAN = float('NAN')


class Interval(object):

    """Definition of the interval type"""

    def __init__(self, lower, upper):
        if NAN in [lower, upper]:
            self.lower = NAN
            self.upper = NAN
        elif lower > upper:
            raise ValueError('''Upper bound lower than the lower bound''')
        else:
            self.lower = lower
            self.upper = upper

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Interval(self.lower + other.lower, self.upper + other.upper)

        return self.__add__(Interval(other, other))

    def __radd__(self, other):
        return self.__add__(Interval(other, other))

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Interval(self.lower - other.upper, self.upper - other.lower)

        return self.__sub__(Interval(other, other))

    def __rsub__(self, other):
        return self.__sub__(Interval(other, other))

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            bounds = [self.lower * other.lower,
                      self.lower * other.upper,
                      self.upper * other.lower,
                      self.upper * other.upper]
            return Interval(min(bounds), max(bounds))

        return self.__mul__(Interval(other, other))

    def __rmul__(self, other):
        return self.__mul__(Interval(other, other))

    def __truediv__(self, other):
        if 0 in other:
            return Interval(-inf, inf)

        bounds = [self.lower / other.lower,
                  self.lower / other.upper,
                  self.upper / other.lower,
                  self.upper / other.upper]

        return Interval(min(bounds), max(bounds))

    def __repr__(self):
        return "[%f, %f]" % (self.lower, self.upper)

    def __contains__(self, number):
        return self.lower <= number <= self.upper

    def __bool__(self):
        return NAN not in [self.lower, self.upper]


    def is_empty(self, number):
        return self.lower <= number <= self.upper


def exp_i(x):
    return Interval(exp(x.lower), exp(x.upper))

def log_i(x):
    if x.upper <= 0:
        return Interval(NAN, NAN)
    elif x.lower <= 0:
        return Interval(-inf, log(x.upper))
    else:
        return Interval(log(x.lower), log(x.upper))


def sqr_i(x):
    bounds = [x.lower**2, x.upper**2]
    if 0 in x:
        return Interval(0, max(bounds))
    else:
        return Interval(min(bounds), max(bounds))

def min_i(x, y):
    return Interval(min(x.lower, y.lower), min(x.upper, y.upper))

def max_i(x, y):
    return Interval(max(x.lower, y.lower), max(x.upper, y.upper))

def func_f(x):
    return sqr_i(x)+2*x-exp_i(x)


if __name__ == "__main__":
    x = Interval(-1, 3)
    y = Interval(2, 5)
    z = Interval(-2, 2)
    print("[-1, 3] + [2, 5] = %s" % (x + y))
    print("[-1, 3] - [2, 5] = %s" % (x - y))
    print("[-1, 3] * [2, 5] = %s" % (x * y))
    print("[-1, 3] / [2, 5] = %s" % (x / y))
    print("[f]([-2, 2]) = %s" % func_f(z))

    print(2 * x)
    print(x * 2)
    print(x + 1)
    print(1 + x)
