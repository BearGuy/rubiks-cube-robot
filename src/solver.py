import sys
import RPi.GPIO as GPIO
import time
import kociemba

from combiner import Combine
from video import Video

from motor import Motor
from motor import Linear
from controller import Control

class Solver:
    def __init__(self,algorithm):
        self.algorithm = algorithm.split() # get list of solve commands from string 
        #self.algorithm = self.state()

    def state(self):
        sides = Video().find_state()
        if not sides:
            print('You did not scan all 6 sides.')
            sys.exit(1)

        unsolved_state = Combine().sides(sides)
        print('Unsolved state: {}'.format(unsolved_state))
        try:
            algorithm = kociemba.solve(unsolved_state)
            length    = len(algorithm.split())
        except Exception as err:
            print('You did not scan all 6 sides correctly.')
            sys.exit(1)

        print('-- SOLUTION --')
        print('Starting position = front: green, top: white')
        print('{0} ({1} moves)'.format(algorithm, length))
        return algorithm

    def solve(self):
        control = Control()
        for command in self.algorithm:
            if command == 'R':
                control.run_R()
            elif command == '2R':
                control.run_2R()
            elif command == "R'":
                control.run_pR()

            elif command == 'L':
                control.run_L()
            elif command == '2L':
                control.run_2L()
            elif command == "L'":
                control.run_pL()

            elif command == 'F':
                control.run_F()
            elif command == '2F':
                control.run_2F()
            elif command == "F'":
                control.run_pF()

            elif command == 'B':
                control.run_B()
            elif command == '2B':
                control.run_2B()
            elif command == "B'":
                control.run_pB()

            elif command == 'U':
                control.run_U()
            elif command == '2U':
                control.run_2U()
            elif command == "U'":
                control.run_pU()

            elif command == 'D':
                control.run_D()
            elif command == '2D':
                control.run_2D()
            elif command == "D'":
                control.run_pD()

            time.sleep(1)

        sys.exit(0)

if __name__ == '__main__':
    Solver("B F R L").solve()
    GPIO.cleanup()
