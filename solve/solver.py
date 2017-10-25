import sys
import RPi.GPIO as GPIO

from motor import Motor

class Solver:
    def __init__(self):
        self.state = 1

    def run(self):
        front_motor = Motor('MF', 3, 5)
        front_motor.rotate(90, 1)
        front_motor.reset()

        GPIO.cleanup() # resets all GPIO ports used by this program
        sys.exit(0)


if __name__ == '__main__':
    Solver().run()