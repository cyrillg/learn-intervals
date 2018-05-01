#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import inf
from myinterval import Interval, exp_i, log_i, sqr_i, sqrt_i, NAN


def cadd(z, x, y):
    """Contractor for addition

    Contractor associated to the primitive operation z = x + y
    """
    z = z & (x + y)
    y = y & (z - x)
    x = x & (z - y)

    return z, x, y


def cmul(z, x, y):
    """Contractor for multiplication

    Contractor associated to the primitive operation z = x * y
    """
    z = z & (x * y)
    y = y & (z / x)
    x = x & (z / y)

    return z, x, y


def cexp(y, x):
    """Contractor for exponential

    Contractor associated to the primitive operation y = exp(x)
    """
    y = y & exp_i(x)
    x = x & log_i(y)

    return y, x


def csqr(y, x):
    """Contractor for square

    Contractor associated to the primitive operation y = x**2
    """
    x_neg = x & Interval(-inf, 0)
    x_pos = x & Interval(0, inf)

    y = (y & sqr_i(x_neg)) | (y & sqr_i(x_pos))

    if y.is_empty():
        return Interval(NAN, NAN), Interval(NAN, NAN)

    x_neg = x_neg & (-1 * sqrt_i(y))
    x_pos = x_pos & sqrt_i(y)

    return y, x_neg | x_pos


if __name__ == "__main__":
    a = Interval(-1, 2)
    b = Interval(3, 4)
    c = Interval(5, 20)
    print(c, a, b)
    print(cadd(c, a, b))
    print(cmul(c, a, b))
    print(cexp(b, a))
    print(csqr(b, a))
