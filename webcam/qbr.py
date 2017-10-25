import sys
import kociemba
import argparse

from combiner import combine
from video import webcam
from normalizer import normalize

class Qbr:

    def __init__(self, normalize):
        self.humanize = normalize

    def run(self):
        state         = webcam.scan()
        if not state:
            print('[QBR SCAN ERROR] Ops, you did not scan in all 6 sides.')
            print('Please try again.')
            sys.exit(1)

        unsolvedState = combine.sides(state)
        try:
            algorithm     = kociemba.solve(unsolvedState)
            length        = len(algorithm.split(' '))
        except Exception as err:
            print('[QBR SOLVE ERROR] Ops, you did not scan in all 6 sides correctly.')
            print('Please try again.')
            sys.exit(1)

        print('-- SOLUTION --')
        print('Starting position:\n    front: green\n    top: white\n')
        print(algorithm, '({0} moves)'.format(length), '\n')

        if self.humanize:
            manual = normalize.algorithm(algorithm)
            for index, text in enumerate(manual):
                print('{}. {}'.format(index+1, text))
        sys.exit(0)

if __name__ == '__main__':
    # define argument parser.
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--normalize', default=False, action='store_true',
            help='Shows the solution normalized. For example "R2" would be: \
                    "Turn the right side 180 degrees".')
    args = parser.parse_args()

    # run Qbr with its arguments.
    Qbr(args.normalize).run()
