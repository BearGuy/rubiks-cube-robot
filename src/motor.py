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

    #"""Rotates the stepper motor given the degrees inputted"""
    #def rotate(self, degrees):
    #    if degrees >= 0:
    #        direct = 1
    #    else:
    #        direct = 0
    #    GPIO.output(self.dir_pin, direct) # set direction for motor to turn, 1 = CW

    #    steps = int(abs(degrees)/1.8)

    #    for i in range(steps):
    #        GPIO.output(self.step_pin, 1)
    #        sleep(0.001)
    #        GPIO.output(self.step_pin, 0)
    #        sleep(0.001)
    #        #print("step {}".format(i))
    #    sleep(0.5)


class Motor(Stepper):
    def new_func(self):
        return

class Linear(Stepper):
    """Create Linear Object"""
    def __init__(self, step_pin, dir_pin, position):
        GPIO.setmode(GPIO.BOARD)  # choose BCM or BOARD
        GPIO.setup(dir_pin, GPIO.OUT)
        GPIO.setup(step_pin, GPIO.OUT)

        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.position = position 

    #"""Add Move Function"""
    #def move(self, position_new):
    #    if self.position == 1 and position_new == 0:
    #        self.rotate(90)
    #        self.position = 0
    #    if self.position == 0 and position_new == 1:
    #        self.rotate(-90)
    #        self.position = 1

