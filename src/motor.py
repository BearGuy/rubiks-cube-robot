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

class Motor(Stepper):
    """Create Motor Object"""
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
