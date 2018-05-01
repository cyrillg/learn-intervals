#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mycontractor import cadd, cmul, cexp, csqr
from math import inf
from myinterval import Interval

if __name__ == "__main__":
    R1 = Interval(0, inf)
    R2 = Interval(0, inf)
    R = Interval(-inf, inf)
    E = Interval(23, 26)
    I = Interval(4, 8)
    I2 = Interval(-inf, inf)
    U1 = Interval(10, 11)
    U2 = Interval(14, 17)
    P = Interval(124, 130)
    print("Before contraction:")
    print("R1 =", R1, ", R2 =", R2, ", E =", E,
          ", I =", I, ", U1 =", U1, ", U2 =", U2)
    for i in range(10):
        R, R1, R2 = cadd(R, R1, R2)
        E, R, I = cmul(E, R, I)
        P, E, I = cmul(P, E, I)
        E, U1, U2 = cadd(E, U1, U2)
        U1, R1, I = cmul(U1, R1, I)
        U2, R2, I = cmul(U2, R2, I)
        I2, I = csqr(I2, I)
        P, R, I2 = cmul(P, R, I2)
    print("After contraction:")
    print("R1 =", R1, ", R2 =", R2, ", E =", E,
          ", I =", I, ", U1 =", U1, ", U2 =", U2)
