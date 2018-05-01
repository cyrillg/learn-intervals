#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from vibes import *
from math import inf
from mybox import Box
from myinterval import Interval, sqr_i
from mycontractor import cadd, csqr


def cin_ring(x, y, cx, cy, r):
    a = x - cx
    b = y - cy
    a2 = sqr_i(a)
    b2 = sqr_i(b)
    r2 = sqr_i(r)
    r2, a2, b2 = cadd(r2, a2, b2)
    a2, a = csqr(a2, a)
    b2, b = csqr(b2, b)
    x, a, cx = cadd(x, a, cx)
    y, b, cy = cadd(y, b, cy)

    return x, y


def sivia(P, cx, cy, r, delta):
    if P.width()[0] < delta:
        return
    vibes.drawBox(P.intvl_list[0].lower,
                  P.intvl_list[0].upper,
                  P.intvl_list[1].lower,
                  P.intvl_list[1].upper,
                  'black[cyan]')
    P.intvl_list[0], P.intvl_list[1] = cin_ring(P.intvl_list[0],
                                                P.intvl_list[1],
                                                cx,
                                                cy,
                                                r)
    vibes.drawBox(P.intvl_list[0].lower,
                  P.intvl_list[0].upper,
                  P.intvl_list[1].lower,
                  P.intvl_list[1].upper,
                  '[yellow]')
    sivia(P.left(), cx, cy, r, delta)
    sivia(P.right(), cx, cy, r, delta)


if __name__ == "__main__":
    vibes.beginDrawing()
    vibes.newFigure('P')
    vibes.setFigureProperties({'x': 0, 'y': 0, 'width': 800, 'height': 500})
    r = Interval(4, 5)
    x = Interval(-10, 10)
    y = Interval(-10, 10)
    cx = Interval(1, 3)
    cy = Interval(2, 4)

    delta = .3
    sivia(Box([x, y]), cx, cy, r, delta)
    vibes.endDrawing()



