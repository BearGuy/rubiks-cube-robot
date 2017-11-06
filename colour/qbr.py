import sys
import kociemba
import argparse

from combiner import combine
from video import webcam
from normalizer import normalize

class Qbr:

    def __init__(self, humanize):
        return

    def run(self):
        state         = webcam.scan()
        if not state:
            print('[QBR SCAN ERROR] You did not scan in all 6 sides.')
            print('Please try again.')
            sys.exit(1)

        unsolvedState = combine.sides(state)
        print('Unsolved state: {}'.format(unsolvedState))
        try:
            algorithm     = kociemba.solve(unsolvedState)
            length        = len(algorithm.split(' '))
        except Exception as err:
            print('[QBR SOLVE ERROR] You did not scan in all 6 sides correctly.')
            print('Please try again.')
            sys.exit(1)

        print('-- SOLUTION --')
        print('Starting position:\n    front: green\n    top: white\n')
        print(algorithm, '({0} moves)'.format(length), '\n')
        sys.exit(0)

if __name__ == '__main__':
    # run Qbr
    Qbr().run()
