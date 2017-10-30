import sys
import RPi.GPIO as GPIO
import time

from motor import Motor
from motor import Linear

class Solver:
    def __init__(self,algorithm):
        self.state = 1
        self.algorithm = algorithm.split() # get list of solve commands from string 
        self.motor_right = Motor('MR', 5, 3)
        # self.linear_right = Linear('LR', -1, -1)

    def solve(self):
        for command in self.algorithm:
            if command == 'R':
                self.run_R()
            elif command == '2R':
                self.run_2R()
            elif command == "R'":
                self.run_pR()

            elif command == 'L':
                self.run_L()
            elif command == '2L':
                self.run_2L()
            elif command == "L'":
                self.run_pL()

            elif command == 'F':
                self.run_F()
            elif command == '2F':
                self.run_2F()
            elif command == "F'":
                self.run_pF()

            elif command == 'B':
                self.run_B()
            elif command == '2B':
                self.run_2B()
            elif command == "B'":
                self.run_pB()

            elif command == 'U':
                self.run_U()
            elif command == '2U':
                self.run_2U()
            elif command == "U'":
                self.run_pU()

            elif command == 'D':
                self.run_D()
            elif command == '2D':
                self.run_2D()
            elif command == "D'":
                self.run_pD()

            time.sleep(1)

        GPIO.cleanup() # resets all GPIO ports used by this program
        sys.exit(0)

    def run_R(self):
        self.motor_right.rotate(90)
        # self.linear_right.move()
        self.motor_right.rotate(-90)
        # self.linear_right.move()
    def run_pR(self):
        self.motor_right.rotate(-90)
        # self.linear_right.move()
        self.motor_right.rotate(90)
        # self.linear_right.move()
    def run_2R(self):
        self.motor_right.rotate(180)

    def run_L(self):
        self.motor_left.rotate(90)
        # self.linear_left.move()
        self.motor_left.rotate(-90)
        # self.linear_left.move()
    def run_pL(self):
        self.motor_left.rotate(-90)
        # self.linear_left.move()
        self.motor_left.rotate(90)
        # self.linear_left.move()
    def run_2L(self):
        self.motor_left.rotate(180)

    def run_F(self):
        self.motor_front.rotate(90)
        # self.linear_front.move()
        self.motor_front.rotate(-90)
        # self.linear_front.move()
    def run_pF(self):
        self.motor_front.rotate(-90)
        # self.linear_front.move()
        self.motor_front.rotate(90)
        # self.linear_front.move()
    def run_2F(self):
        self.motor_front.rotate(180)

    def run_B(self):
        self.motor_back.rotate(90)
        # self.linear_back.move()
        self.motor_back.rotate(-90)
        # self.linear_back.move()
    def run_pB(self):
        self.motor_back.rotate(-90)
        # self.linear_back.move()
        self.motor_back.rotate(90)
        # self.linear_back.move()
    def run_2B(self):
        self.motor_back.rotate(180)

if __name__ == '__main__':
    Solver("R'").solve()
