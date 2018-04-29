#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import inf
from myinterval import Interval, func_f, min_i
from vibes import *


def gen_x(k, d, x_min):
    return x_min + d * Interval(k, k + 1)


def drawtube(v_min, v_max, d, color):
    k = 0
    x = gen_x(k, d, v_min)
    m = Interval(inf, inf)
    while x.upper <= v_max:
        y = func_f(x)
        vibes.drawBox(x.lower, x.upper, y.lower, y.upper, color)
        x = gen_x(k, d, -2)
        k += 1
        m = min_i(m, y)
    return m


if __name__ == "__main__":
    vibes.beginDrawing()
    vibes.newFigure('myminimizer')
    vibes.setFigureProperties({'x': 0, 'y': 0, 'width': 1600, 'height': 1000})

    print(drawtube(-2, 2, 0.5, '[blue]'))
    print(drawtube(-2, 2, 0.05, '[yellow]'))
    print(drawtube(-2, 2, 0.005, '[red]'))
    print(drawtube(-2, 2, 0.0005, '[grey]'))
    vibes.endDrawing()
