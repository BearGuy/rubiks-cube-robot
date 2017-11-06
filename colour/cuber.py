import sys
import kociemba

from combiner import Combine
from video import Video

class Qbr:

    def __init__(self):
        return

    def run(self):
        sides = Video().scan()
        if not sides:
            print('[QBR SCAN ERROR] You did not scan in all 6 sides.')
            print('Please try again.')
            sys.exit(1)

        unsolved_state = Combine().sides(sides)
        print('Unsolved state: {}'.format(unsolved_state))
        try:
            algorithm     = kociemba.solve(unsolved_state)
            length        = len(algorithm.split())
        except Exception as err:
            print('[QBR SOLVE ERROR] You did not scan in all 6 sides correctly.')
            print('Please try again.')
            sys.exit(1)

        print('-- SOLUTION --')
        print('Starting position = front: green, top: white')
        print('{0} ({1} moves)'.format(algorithm, length))
        return algorithm

if __name__ == '__main__':
    # run Qbr
    Qbr().run()
