from time import sleep
import RPi.GPIO as GPIO

class Stepper:
    """Create Stepper Object"""
    def __init__(self, step_pin, dir_pin):
        GPIO.setmode(GPIO.BOARD)  # choose BCM or BOARD
        GPIO.setup(dir_pin, GPIO.OUT)
        GPIO.setup(step_pin, GPIO.OUT)

        self.step_pin = step_pin
        self.dir_pin = dir_pin
        # self.degrees = 0

    """Rotates the stepper motor given the degrees inputted"""
    def rotate(self, degrees):
        if degrees >= 0:
            direct = 1
        else:
            direct = 0
        GPIO.output(self.dir_pin, direct) # set direction for motor to turn, 1 = CW

        steps = int(abs(degrees)/1.8)

        for i in range(steps):
            GPIO.output(self.step_pin, 1)
            sleep(0.001)
            GPIO.output(self.step_pin, 0)
            sleep(0.001)
            print("step {}".format(i))
        sleep(0.1)

        # self.degrees += degrees

    """Resets the to the motor to 0 degrees"""
    # def reset(self):
        # self.degrees = self.degrees % 360
        # self.rotate(-self.degrees) # rotate backwards to starting position
        # self.degrees = 0


class Motor(Stepper):
    def new_func(self):
        return

class Linear(Stepper):
    def move(self, direct):
        return
