import sys
import RPi.GPIO as GPIO
import time

from motor import Motor
from motor import Linear

class Solver:
    def __init__(self,algorithm):
        self.algorithm = algorithm.split() # get list of solve commands from string 

        self.motor_right = Motor(8, 10)
        self.motor_left = Motor(3, 5)
        # self.motor_front = Motor(3, 5)
        # self.motor_back = Motor(8, 10)

        self.linear_right = Linear(21, 23)
        self.linear_left = Linear(22, 24)
        # self.linear_front = Linear(3, 5)
        # self.linear_back = Linear(8, 10)

    def rotate_2(self, motor_1, motor_2, degrees):
        if degrees >= 0:
            direct = 1
        else:
            direct = 0
        GPIO.output(motor_1.dir_pin, direct) # set direction for motor to turn, 1 = CW
        GPIO.output(motor_2.dir_pin, direct^1) # set direction for motor to turn, 1 = CW

        steps = int(abs(degrees)/1.8)

        for i in range(steps):
            GPIO.output(motor_1.step_pin, 1)
            GPIO.output(motor_2.step_pin, 1)
            time.sleep(0.001)
            GPIO.output(motor_1.step_pin, 0)
            GPIO.output(motor_2.step_pin, 0)
            time.sleep(0.001)
            print("step {}".format(i))
        time.sleep(0.1)

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
        self.linear_right.move(0)
        self.motor_right.rotate(-90)
        self.linear_right.move(1)
    def run_pR(self):
        self.motor_right.rotate(-90)
        self.linear_right.move(0)
        self.motor_right.rotate(90)
        self.linear_right.move(1)
    def run_2R(self):
        self.motor_right.rotate(180)

    def run_L(self):
        self.motor_left.rotate(90)
        self.linear_left.move(0)
        self.motor_left.rotate(-90)
        self.linear_left.move(1)
    def run_pL(self):
        self.motor_left.rotate(-90)
        self.linear_left.move(0)
        self.motor_left.rotate(90)
        self.linear_left.move(1)
    def run_2L(self):
        self.motor_left.rotate(180)

    def run_F(self):
        self.motor_front.rotate(90)
        self.linear_front.move(0)
        self.motor_front.rotate(-90)
        self.linear_front.move(1)
    def run_pF(self):
        self.motor_front.rotate(-90)
        self.linear_front.move(0)
        self.motor_front.rotate(90)
        self.linear_front.move(1)
    def run_2F(self):
        self.motor_front.rotate(180)

    def run_B(self):
        self.motor_back.rotate(90)
        self.linear_back.move(0)
        self.motor_back.rotate(-90)
        self.linear_back.move(1)
    def run_pB(self):
        self.motor_back.rotate(-90)
        self.linear_back.move(0)
        self.motor_back.rotate(90)
        self.linear_back.move(1)
    def run_2B(self):
        self.motor_back.rotate(180)

    def run_U(self):
        self.linear_front.move(0)
        self.linear_back.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90) # rotate away from default orientation

        self.linear_front.move(1)
        self.linear_back.move(1)
        
        self.linear_right.move(0)
        self.linear_left.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90)

        self.linear_right.move(1)
        self.linear_left.move(1)

        self.motor_back.rotate(90)  # do the actual rotation

        self.linear_front.move(0)
        self.linear_back.move(0)
        self.motor_back.rotate(90)

        self.rotate_2(self.motor_right, self.motor_left, -90)

        self.linear_front.move(1)
        self.linear_back.move(1)

        self.linear_right.move(0)
        self.linear_left.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90)

        self.linear_right.move(1)
        self.linear_left.move(1)
    def run_pU(self):
        self.linear_front.move(0)
        self.linear_back.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90) # rotate away from default orientation

        self.linear_front.move(1)
        self.linear_back.move(1)
        
        self.linear_right.move(0)
        self.linear_left.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90)

        self.linear_right.move(1)
        self.linear_left.move(1)

        self.motor_back.rotate(180)  # do the actual rotation

        self.linear_front.move(0)
        self.linear_back.move(0)

        self.rotate_2(self.motor_right, self.motor_left, -90)

        self.linear_front.move(1)
        self.linear_back.move(1)

        self.linear_right.move(0)
        self.linear_left.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90)

        self.linear_right.move(1)
        self.linear_left.move(1)
    def run_2U(self):
        self.linear_front.move(0)
        self.linear_back.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90) # rotate away from default orientation

        self.linear_front.move(1)
        self.linear_back.move(1)
        
        self.linear_right.move(0)
        self.linear_left.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90)

        self.linear_right.move(1)
        self.linear_left.move(1)

        self.motor_back.rotate(-90)  # do the actual rotation

        self.linear_front.move(0)
        self.linear_back.move(0)
        self.motor_back.rotate(90)

        self.rotate_2(self.motor_right, self.motor_left, -90)

        self.linear_front.move(1)
        self.linear_back.move(1)

        self.linear_right.move(0)
        self.linear_left.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90)

        self.linear_right.move(1)
        self.linear_left.move(1)

    def run_D(self):
        self.linear_front.move(0)
        self.linear_back.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90) # rotate away from default orientation

        self.linear_front.move(1)
        self.linear_back.move(1)
        
        self.linear_right.move(0)
        self.linear_left.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90)

        self.linear_right.move(1)
        self.linear_left.move(1)

        self.motor_front.rotate(90)  # do the actual rotation

        self.linear_front.move(0)
        self.linear_back.move(0)
        self.motor_front.rotate(90)

        self.rotate_2(self.motor_right, self.motor_left, -90)

        self.linear_front.move(1)
        self.linear_back.move(1)

        self.linear_right.move(0)
        self.linear_left.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90)

        self.linear_right.move(1)
        self.linear_left.move(1)
    def run_pD(self):
        self.linear_front.move(0)
        self.linear_back.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90) # rotate away from default orientation

        self.linear_front.move(1)
        self.linear_back.move(1)
        
        self.linear_right.move(0)
        self.linear_left.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90)

        self.linear_right.move(1)
        self.linear_left.move(1)

        self.motor_front.rotate(-90)  # do the actual rotation

        self.linear_front.move(0)
        self.linear_back.move(0)
        self.motor_front.rotate(90)

        self.rotate_2(self.motor_right, self.motor_left, -90)

        self.linear_front.move(1)
        self.linear_back.move(1)

        self.linear_right.move(0)
        self.linear_left.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90)

        self.linear_right.move(1)
        self.linear_left.move(1)
    def run_2D(self):
        self.linear_front.move(0)
        self.linear_back.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90) # rotate away from default orientation

        self.linear_front.move(1)
        self.linear_back.move(1)
        
        self.linear_right.move(0)
        self.linear_left.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90)

        self.linear_right.move(1)
        self.linear_left.move(1)

        self.motor_front.rotate(180)  # do the actual rotation

        self.linear_front.move(0)
        self.linear_back.move(0)

        self.rotate_2(self.motor_right, self.motor_left, -90)

        self.linear_front.move(1)
        self.linear_back.move(1)

        self.linear_right.move(0)
        self.linear_left.move(0)

        self.rotate_2(self.motor_right, self.motor_left, 90)

        self.linear_right.move(1)
        self.linear_left.move(1)

    def test_double(self):
        self.rotate_2(self.motor_front, self.motor_back, 90) # rotate away from default orientation
        GPIO.cleanup()

if __name__ == '__main__':
    Solver("2L 2L 2L").solve()
