#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from myinterval import Interval
from copy import deepcopy

NAN = float('NAN')


class Box(object):
    def __init__(self, intvl_list):
        if intvl_list:
            self.intvl_list = intvl_list
        else:
            raise ValueError("A Box must have at least 1 dimension")

    def __repr__(self):
        descr = str(self.intvl_list[0])
        if len(self.intvl_list) == 1:
            return descr

        for intvl in self.intvl_list[1:]:
            descr += "\nX %s" % str(intvl)

        return descr


    def width(self):
        for intvl in self.intvl_list:
            if intvl.is_empty():
                return NAN, -1

        len_list = [intvl.width() for intvl in self.intvl_list]
        max_val = max(len_list)
        max_idx = len_list.index(max_val)
        return max_val, max_idx


    def left(self):
        w, idx = self.width()
        left_box = deepcopy(self)
        left_box.intvl_list[idx].upper -= w / 2.
        return left_box


    def right(self):
        w, idx = self.width()
        right_box = deepcopy(self)
        right_box.intvl_list[idx].lower += w / 2.
        return right_box


if __name__ == "__main__":
    x = Interval(-3, 6)
    y = Interval(5, 9)
    b = Box([x, y])
    w, idx = b.width()
    print("B: %s" % b)
    print()
    print("B left: %s" % b.left())
    print()
    print("B right: %s" % b.right())
