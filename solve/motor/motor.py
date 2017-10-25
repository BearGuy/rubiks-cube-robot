from time import sleep             # lets us have a delay
import RPi.GPIO as GPIO            # import RPi.GPIO module

## legend
# MB = Back motor
# MBL = Translational back motor
# MR = Right motor
# MRL = Translational right motor
# ML = Left Motor
# MLL = Translational left motor
# MF = Front Motor
# MFL = Translational front motor

## Back Motors

# MBL_step_pin = the number of the raspberry pi pin connected to step pin on the motor 1 (linear) driver
# MBL_dir_pin = the number of the raspberry pi pin connected to the dir pin on the motor 1 (linear) driver

# MB_step_pin = 5 # the number of the raspberry pi pin connected to step pin on motor driver
# MB_dir_pin = 3 # the number of the raspberry pi pin connected to the dir pin on the motor driver

# dist = # number of steps required to translate arm adequate distance
# dir input should be 1 for CW, 0 for CCW, entres degrees in degrees of rotation

class Motor:
    """Create Motor Object"""
    def __init__(self, role, step_pin, dir_pin):
        GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD
        GPIO.setup(3, GPIO.OUT)           # set GPIO24 as an output
        GPIO.setup(5, GPIO.OUT)           # set GPIO23 as an output

        self.role = role
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.degrees = 0

    """Rotates a side of the cube given the degrees and direction inputted"""
    def rotate(self, degrees, direct):
        GPIO.output(self.dir_pin, direct) # set direction for motor to drive, 1 = CW

        steps = int(degrees/1.8)

        for i in range(steps):
            GPIO.output(self.step_pin, 1)
            sleep(0.001)
            GPIO.output(self.step_pin, 0)
            sleep(0.001)
            print("step {}".format(i))

        self.degrees = degrees

    """Resets the claw attached to the motor"""
    def reset(self):
        if self.degrees % 180 == 90:
            self.rotate(90, 0)
