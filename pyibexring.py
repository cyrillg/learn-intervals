#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pyibex import *
from vibes import *
from math import inf


class myCtc(Ctc):
    def __init__(self):
        Ctc.__init__(self, 2)

    def contract(self, X):
        x, y = X[0], X[1]
        cx, cy, r = Interval(1, 3), Interval(2, 4), Interval(4, 5)
        a, b = x - cx, y - cy
        a2, b2, r2 = sqr(a), sqr(b), sqr(r)
        bwd_add(r2, a2, b2)
        bwd_sqr(a2, a)
        bwd_sqr(b2, b)
        bwd_sub(a, x, cx)
        bwd_sub(b, y, cy)


if __name__ == "__main__":
    vibes.beginDrawing()
    vibes.newFigure('one ring with pyibex')
    vibes.setFigureProperties({'x': 200, 'y': 100, 'width': 800, 'height': 800})

    X0 = IntervalVector(2, [-10, 10])
    ctc = myCtc()
    pySIVIA(X0, ctc, 0.5)

    #  delta = .3
    #  sivia(Box([x, y]), cx, cy, r, delta)
    vibes.endDrawing()
