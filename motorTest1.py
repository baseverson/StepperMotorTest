#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)

PIN_HIGH = GPIO.HIGH
PIN_LOW = GPIO.LOW
#PIN_HIGH = GPIO.LOW
#PIN_LOW = GPIO.HIGH



# init list with pin numbers

#pinList = [3, 5, 7, 11, 13, 15, 19, 21]
pinList = [12,16, 20, 21]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, PIN_LOW)

# time to sleep between operations in the main loop

SleepTimeL = 0.005

# main loop

try:

    while True:
        for i in pinList:
            GPIO.output(i, PIN_HIGH)
            time.sleep(SleepTimeL);
            GPIO.output(i, PIN_LOW)

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

