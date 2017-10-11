import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(24, GPIO.OUT)           # set GPIO24 as an output   
GPIO.setup(23, GPIO.OUT)           # set GPIO23 as an output   
 
## legend
# MB = Back motor
# MBL = Translational back motor
# MR = Right motor
# MRL = Translational right motor
# ML = Left Motor
# MLL = Translational left motor

## Back Motors

# MBL_step_pin = # the number of the raspberry pi pin connected to step pin on the motor 1 (linear) driver 
# MBL_dir_pin = # the number of the raspberry pi pin connected to the dir pin on the motor 1 (linear) driver
# dist= # number of steps required to translate arm adequate distance

MB_step_pin = # the number of the raspberry pi pin connected to step pin on motor driver 
MB_dir_pin = # the number of the raspberry pi pin connected to the dir pin on the motor driver
# intialize MB step?

def MB_rot(MB_step,degrees,dir): #dir input should be 1 for CW, 0 for CCW, entres degrees in degrees of rotation
  
  GPIO.output(MB_dir_pin,dir) # set direction for motor to drive, 1 = CW

  steps=(degrees/1.8)-1

  for i in range (0:steps):
    if MB_step == 1: 
      GPIO.output(MB_step_pin,0)
      MB_step=0
    else:
      GPIO.output(MB_step_pin,1)
      MB_step=1

  return MB_step


GPIO.cleanup()                 # resets all GPIO ports used by this program  
