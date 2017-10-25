import sys
import json

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
