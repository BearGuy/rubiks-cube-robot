import time
import RPi.GPIO as GPIO
from motor import Motor
from motor import Linear

class Control:
    def __init__(self):
        self.motor_right = Motor(3, 5)
        self.motor_left  = Motor(8, 10)
        self.motor_front = Motor(11, 12)
        self.motor_back  = Motor(15, 16)

        self.linear_right = Linear(21, 23, 1)
        self.linear_left  = Linear(22, 24, 1)
        self.linear_front = Linear(35, 36, 1)
        self.linear_back  = Linear(29, 31, 1)

    """Rotates the stepper motor by the degrees inputted"""
    def rotate(self, motor, degrees):
        if degrees >= 0:
            direct = 0
        else:
            direct = 1
        # set direction for motor to turn, 0 = CCW for motor, CW for cube
        GPIO.output(motor.dir_pin, direct)
        steps = int(abs(degrees)/1.8)

        for i in range(steps):
            GPIO.output(motor.step_pin, 1)
            time.sleep(0.01)
            GPIO.output(motor.step_pin, 0)
            time.sleep(0.01)
        time.sleep(0.5)

    """Rotates the 2 stepper motors simultaneously by the degrees inputted"""
    def rotate_2(self, motor_1, motor_2, degrees):
        if degrees >= 0:
            direct = 0
        else:
            direct = 1
        # set direction for motor to turn, 0 = CCW for motor, CW for cube
        GPIO.output(motor_1.dir_pin, direct)
        GPIO.output(motor_2.dir_pin, direct^1)

        steps = int(abs(degrees)/1.8)

        for i in range(steps):
            GPIO.output(motor_1.step_pin, 1)
            GPIO.output(motor_2.step_pin, 1)
            time.sleep(0.01)
            GPIO.output(motor_1.step_pin, 0)
            GPIO.output(motor_2.step_pin, 0)
            time.sleep(0.01)
        time.sleep(0.5)

    def move_2_rotate(self, motor_1, motor_2, degrees):
        if degrees >= 0:
            direct = 0
        else:
            direct = 1
        # set direction for motor to turn, 0 = CCW for motor, CW for cube
        GPIO.output(motor_1.dir_pin, direct)
        GPIO.output(motor_2.dir_pin, direct)

        steps = int(abs(degrees)/1.8)

        for i in range(steps):
            GPIO.output(motor_1.step_pin, 1)
            GPIO.output(motor_2.step_pin, 1)
            time.sleep(0.01)
            GPIO.output(motor_1.step_pin, 0)
            GPIO.output(motor_2.step_pin, 0)
            time.sleep(0.01)
        time.sleep(0.5)

    def move(self, motor, position_new):
        if motor.position == 1 and position_new == 0:
            self.rotate(motor, 90)
            motor.position = 0
        if motor.position == 0 and position_new == 1:
            self.rotate(motor, -90)
            motor.position = 1

    def move_2(self, motor_1, motor_2, position_new):
        if motor_1.position == 1 and motor_2.position == 1 and position_new == 0:
            self.move_2_rotate(motor_1, motor_2, 90)
            motor_1.position = 0
            motor_2.position = 0
        if motor_1.position == 0 and motor_2.position == 0 and position_new == 1:
            self.move_2_rotate(motor_1, motor_2, -90)
            motor_1.position = 1
            motor_2.position = 1

    def run_R(self):
        self.rotate(self.motor_right, 90)
        self.move(self.linear_right, 0)
        self.rotate(self.motor_right, -90)
        self.move(self.linear_right, 1)
    def run_pR(self):
        self.rotate(self.motor_right, -90)
        self.move(self.linear_right, 0)
        self.rotate(self.motor_right, 90)
        self.move(self.linear_right, 1)
    def run_2R(self):
        self.rotate(self.motor_right, 180)

    def run_L(self):
        self.rotate(self.motor_left, 90)
        self.move(self.linear_left, 0)
        self.rotate(self.motor_left, -90)
        self.move(self.linear_left, 1)
    def run_pL(self):
        self.rotate(self.motor_left, -90)
        self.move(self.linear_left, 0)
        self.rotate(self.motor_left, 90)
        self.move(self.linear_left, 1)
    def run_2L(self):
        self.rotate(self.motor_left, 180)

    def run_F(self):
        self.rotate(self.motor_front, 90)
        self.move(self.linear_front, 0)
        self.rotate(self.motor_front, -90)
        self.move(self.linear_front, 1)
    def run_pF(self):
        self.rotate(self.motor_front, -90)
        self.move(self.linear_front, 0)
        self.rotate(self.motor_front, 90)
        self.move(self.linear_front, 1)
    def run_2F(self):
        self.rotate(self.motor_front, 180)

    def run_B(self):
        self.rotate(self.motor_back, 90)
        self.move(self.linear_back, 0)
        self.rotate(self.motor_back, -90)
        self.move(self.linear_back, 1)
    def run_pB(self):
        self.rotate(self.motor_back, -90)
        self.move(self.linear_back, 0)
        self.rotate(self.motor_back, 90)
        self.move(self.linear_back, 1)
    def run_2B(self):
        self.rotate(self.motor_back, 180)

    def run_U(self):
        self.move_2(self.linear_front, self.linear_back, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90) # rotate away from default orientation
        self.move_2(self.linear_front, self.linear_back, 1)
        
        self.move_2(self.linear_right, self.linear_left, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90)
        self.move_2(self.linear_right, self.linear_left, 1)

        self.rotate(self.motor_back, 90) # do the actual rotation

        self.move_2(self.linear_front, self.linear_back, 0)
        self.rotate(self.motor_back, 90)
        self.rotate_2(self.motor_right, self.motor_left, -90)
        self.move_2(self.linear_front, self.linear_back, 1)

        self.move_2(self.linear_right, self.linear_left, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90)
        self.move_2(self.linear_right, self.linear_left, 1)

    def run_pU(self):
        self.move_2(self.linear_front, self.linear_back, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90) # rotate away from default orientation
        self.move_2(self.linear_front, self.linear_back, 1)
        
        self.move_2(self.linear_right, self.linear_left, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90)
        self.move_2(self.linear_right, self.linear_left, 1)

        self.rotate(self.motor_back, -90) # do the actual rotation

        self.move_2(self.linear_front, self.linear_back, 0)
        self.rotate(self.motor_back, 90)
        self.rotate_2(self.motor_right, self.motor_left, -90)
        self.move_2(self.linear_front, self.linear_back, 1)

        self.move_2(self.linear_right, self.linear_left, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90)
        self.move_2(self.linear_right, self.linear_left, 1)

    def run_2U(self):
        self.move_2(self.linear_front, self.linear_back, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90) # rotate away from default orientation
        self.move_2(self.linear_front, self.linear_back, 1)
        
        self.move_2(self.linear_right, self.linear_left, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90)
        self.move_2(self.linear_right, self.linear_left, 1)

        self.rotate(self.motor_back, 180) # do the actual rotation

        self.move_2(self.linear_front, self.linear_back, 0)
        self.rotate_2(self.motor_right, self.motor_left, -90)
        self.move_2(self.linear_front, self.linear_back, 1)

        self.move_2(self.linear_right, self.linear_left, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90)
        self.move_2(self.linear_right, self.linear_left, 1)

    def run_D(self):
        self.move_2(self.linear_front, self.linear_back, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90) # rotate away from default orientation
        self.move_2(self.linear_front, self.linear_back, 1)
        
        self.move_2(self.linear_right, self.linear_left, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90)
        self.move_2(self.linear_right, self.linear_left, 1)

        self.rotate(self.motor_front, 90)  # do the actual rotation

        self.move_2(self.linear_front, self.linear_back, 0)
        self.rotate(self.motor_front, 90)
        self.rotate_2(self.motor_right, self.motor_left, -90)
        self.move_2(self.linear_front, self.linear_back, 1)

        self.move_2(self.linear_right, self.linear_left, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90)
        self.move_2(self.linear_right, self.linear_left, 1)

    def run_pD(self):
        self.move_2(self.linear_front, self.linear_back, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90) # rotate away from default orientation
        self.move_2(self.linear_front, self.linear_back, 1)
        
        self.move_2(self.linear_right, self.linear_left, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90)
        self.move_2(self.linear_right, self.linear_left, 1)

        self.rotate(self.motor_front, -90)  # do the actual rotation

        self.move_2(self.linear_front, self.linear_back, 0)
        self.rotate(self.motor_front, 90)
        self.rotate_2(self.motor_right, self.motor_left, -90)
        self.move_2(self.linear_front, self.linear_back, 1)

        self.move_2(self.linear_right, self.linear_left, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90)
        self.move_2(self.linear_right, self.linear_left, 1)

    def run_2D(self):
        self.move_2(self.linear_front, self.linear_back, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90) # rotate away from default orientation
        self.move_2(self.linear_front, self.linear_back, 1)
        
        self.move_2(self.linear_right, self.linear_left, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90)
        self.move_2(self.linear_right, self.linear_left, 1)

        self.rotate(self.motor_front, 180) # do the actual rotation

        self.move_2(self.linear_front, self.linear_back, 0)
        self.rotate_2(self.motor_right, self.motor_left, -90)
        self.move_2(self.linear_front, self.linear_back, 1)

        self.move_2(self.linear_right, self.linear_left, 0)
        self.rotate_2(self.motor_right, self.motor_left, 90)
        self.move_2(self.linear_right, self.linear_left, 1)
