#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyibex import *
from pyibex import geometry
import numpy as np
from vibes import *

Marks = [[6, 12], [-2, -5], [-3, 10], [3, 4]]
D = [Interval(10, 13), Interval(8, 10), Interval(5, 7), Interval(6, 8)]
Alpha = [Interval(0.5, 1), Interval(-3, -1.5), Interval(1, 2), Interval(2, 3)]

vibes.beginDrawing()
vibes.newFigure("Loc pie")
vibes.setFigureProperties({'x': 100, 'y': 100, 'width': 1200, 'height': 700})
#  vibes.axisEqual()

P = IntervalVector([[-20, 20], [-20, 20]])
seps = []
for m, d, alpha in zip(Marks[:-1], D[:-1], Alpha[:-1]):
    sep1 = geometry.SepPolarXY(d, alpha)
    fforw=Function("v1", "v2", "(%f-v1;%f-v2)" % (m[0], m[1]))
    fback=Function("p1", "p2", "(%f-p1;%f-p2)" % (m[0], m[1]))
    sep = SepTransform(sep1, fback, fforw)
    seps.append(sep)

sep = SepQInterProjF(seps)
sep.q = 0

pySIVIA(P, sep, .1)

for m in Marks:
    vibes.drawCircle(m[0], m[1], .3, 'yellow[black]')

vibes.endDrawing()
