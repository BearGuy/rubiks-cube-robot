import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD  
GPIO.setup(3, GPIO.OUT)           # set GPIO24 as an output   
GPIO.setup(5, GPIO.OUT)           # set GPIO23 as an output   
 
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

MB_step_pin = 5 # the number of the raspberry pi pin connected to step pin on motor driver 
MB_dir_pin = 3 # the number of the raspberry pi pin connected to the dir pin on the motor driver

def MB_rot(degrees,direct): #dir input should be 1 for CW, 0 for CCW, entres degrees in degrees of rotation
  
  GPIO.output(MB_dir_pin,direct) # set direction for motor to drive, 1 = CW

  steps=(degrees/1.8)
    
  steps = int(steps)
  for i in range(steps):
    GPIO.output(MB_step_pin,1)
    sleep(0.001)
    GPIO.output(MB_step_pin,0)
    sleep(0.001)
    print("step {}".format(i))

MB_rot(360,1)


GPIO.cleanup()                 # resets all GPIO ports used by this program  
