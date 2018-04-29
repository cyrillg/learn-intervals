#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from vibes import *
from mybox import Box
from myinterval import Interval, exp_i


def func_f(t, p1, p2):
    return p1 * exp_i(p2 * t)


def test(P, T, Y):
    b = Interval(0, 0)
    for i, Yi in enumerate(Y):
        curr_intvl = func_f(T[i], P.intvl_list[0], P.intvl_list[1])
        if curr_intvl.subset(Yi):
            b += 1
        elif not (curr_intvl & Yi).is_empty():
            b += Interval(0, 1)
    return b


def sivia(P, T, Y, delta, R):
    b = test(P, T, Y)
    vibes.selectFigure('P')
    if b.upper < len(Y) - R:
        vibes.drawBox(P.intvl_list[0].lower,
                      P.intvl_list[0].upper,
                      P.intvl_list[1].lower,
                      P.intvl_list[1].upper,
                      '[cyan]')
    elif b.lower >= len(Y) - R:
        vibes.drawBox(P.intvl_list[0].lower,
                      P.intvl_list[0].upper,
                      P.intvl_list[1].lower,
                      P.intvl_list[1].upper,
                      '[red]')
    elif P.width()[0] < delta:
        vibes.drawBox(P.intvl_list[0].lower,
                      P.intvl_list[0].upper,
                      P.intvl_list[1].lower,
                      P.intvl_list[1].upper,
                      'yellow[yellow]')
        draw_output(P)
    else:
        sivia(P.left(), T, Y, delta, R)
        sivia(P.right(), T, Y, delta, R)

def draw_output(P):
    t = 0.
    dt = .05
    vibes.selectFigure('Y')
    while t < 5.:
        T = Interval(t, t + dt)
        y = P.intvl_list[0] * exp_i(P.intvl_list[1] * T)
        vibes.drawBox(T.lower, T.upper, y.lower, y.upper, 'green[green]')
        t = t + dt


if __name__ == "__main__":
    vibes.beginDrawing()
    vibes.newFigure('P')
    vibes.setFigureProperties({'x': 0, 'y': 0, 'width': 1600, 'height': 1000})
    vibes.newFigure('Y')
    vibes.setFigureProperties({'x': 0, 'y': 0, 'width': 1600, 'height': 1000})

    DELTA = 0.01
    R = 0
    T = [.2, 1., 2., 4.]
    Y = [Interval(1.5, 2.),
         Interval(.7, .8),
         Interval(.1, .3),
         Interval(-0.1, .03)]
    P = Box([Interval(-3., 3.),
             Interval(-3., 3.)])

    sivia(P, T, Y, DELTA, R)

    vibes.selectFigure('Y')
    for i, s in enumerate(Y):
        vibes.drawBox(T[i]-0.01, T[i]+0.01,
                      s.lower, s.upper, 'red[red]')

    vibes.endDrawing()
