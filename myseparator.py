#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
        xb, yb = cin_ring(xb, yb, cx, cy, Interval(r.upper, inf))
        x = xa | xb
        y = ya | yb

    return x, y


def sep(x, y, outer):
    cx1 = Interval(1, 1)
    cy1 = Interval(2, 2)
    r1 = Interval(4, 5)
    x, y = sin_ring(x, y, cx1, cy1, r1, outer)
    return x, y


def sivia(P, delta):
    if P.width()[0] < delta:
        return
    vibes.drawBox(P.intvl_list[0].lower,
                  P.intvl_list[0].upper,
                  P.intvl_list[1].lower,
                  P.intvl_list[1].upper,
                  'black[cyan]')
    P.intvl_list[0], P.intvl_list[1] = sep(P.intvl_list[0],
                                           P.intvl_list[1],
                                           True)
    vibes.drawBox(P.intvl_list[0].lower,
                  P.intvl_list[0].upper,
                  P.intvl_list[1].lower,
                  P.intvl_list[1].upper,
                  'blue[magenta]')
    P.intvl_list[0], P.intvl_list[1] = sep(P.intvl_list[0],
                                           P.intvl_list[1],
                                           False)
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
    #  x = Interval(-4.1, -3.7)
    #  y = Interval(2., 2.6)

    delta = .3
    sivia(Box([x, y]), delta)
    vibes.endDrawing()
