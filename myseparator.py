#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from vibes import *
from math import inf
from mybox import Box
from myinterval import Interval, sqr_i
from mycontractor import cadd, csqr
from myring import cin_ring


def sin_ring(x, y, cx, cy, r, outer):
    if outer:
        x, y = cin_ring(x, y, cx, cy, r)
    else:
        xa, ya = x, y
        xb, yb = x, y
        xa, ya = cin_ring(xa, ya, cx, cy, Interval(-1, r.lower))
        #  print("Ba:", xa, ya)
        xb, yb = cin_ring(xb, yb, cx, cy, Interval(r.upper, inf))
        #  print("Bb:", xb, yb)
        x = xa | xb
        y = ya | yb

    return x, y


def sep(x, y, outer):
    cx1 = Interval(1, 1)
    cy1 = Interval(2, 2)
    r1 = Interval(4, 5)
    cx2 = Interval(2, 2)
    cy2 = Interval(5, 5)
    r2 = Interval(5, 6)

    x1, y1 = x, y
    x2, y2 = x, y

    x1, y1 = sin_ring(x1, y1, cx1, cy1, r1, outer)
    #  print("B1:", x1, y1)
    x2, y2 = sin_ring(x2, y2, cx2, cy2, r2, outer)
    #  print("B2:", x2, y2)

    if outer:
        x, y = x1 & x2, y1 & y2
    else:
        x, y = x1 | x2, y1 | y2

    return x, y


def sivia(P, delta):
    if P.width()[0] < delta or P.is_empty():
        return
    vibes.drawBox(P.intvl_list[0].lower,
                  P.intvl_list[0].upper,
                  P.intvl_list[1].lower,
                  P.intvl_list[1].upper,
                  'black[cyan]')
    #  print("Start:")
    #  print(P)
    #  print("Outer:")
    P.intvl_list[0], P.intvl_list[1] = sep(P.intvl_list[0],
                                           P.intvl_list[1],
                                           True)
    #  print(P)
    vibes.drawBox(P.intvl_list[0].lower,
                  P.intvl_list[0].upper,
                  P.intvl_list[1].lower,
                  P.intvl_list[1].upper,
                  'blue[magenta]')
    #  print("Inner:")
    P.intvl_list[0], P.intvl_list[1] = sep(P.intvl_list[0],
                                           P.intvl_list[1],
                                           False)
    #  print(P)
    vibes.drawBox(P.intvl_list[0].lower,
                  P.intvl_list[0].upper,
                  P.intvl_list[1].lower,
                  P.intvl_list[1].upper,
                  '[yellow]')
    sivia(P.left(), delta)
    sivia(P.right(), delta)


if __name__ == "__main__":
    vibes.beginDrawing()
    vibes.newFigure('P')
    vibes.setFigureProperties({'x': 0, 'y': 0, 'width': 800, 'height': 500})
    x = Interval(-10, 10)
    y = Interval(-10, 10)
    #  x = Interval(4., 6.)
    #  y = Interval(-2., 2.)

    delta = .01
    sivia(Box([x, y]), delta)
    vibes.endDrawing()
