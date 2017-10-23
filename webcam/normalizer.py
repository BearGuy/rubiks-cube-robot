#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename      : normalizer.py
# Author        : Kim K
# Created       : Sat, 30 Jan 2016
# Last Modified : Mon, 01 Feb 2016


from sys import exit as Die
try:
    import sys
    import json
except ImportError as err:
    Die(err)


class Normalizer:

    def algorithm(self, alg):
        """ Noramlize an algorithm from the
        json-written manual.

        :param alg: The algorithm itself
        :returns: list
        """
        with open('solve-manual.json') as f:
            manual = json.load(f)

        solution = []
        for notation in alg.split(' '):
            solution.append(manual[notation])
        return solution

normalize = Normalizer()