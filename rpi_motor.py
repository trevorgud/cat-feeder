import RPi.GPIO as GPIO
import datetime
import time

class PiGpioMotor():
  def __init__(self, pin, rpm):
    self._rpm = rpm
    self._pin = pin
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.Board)
    GPIO.setup(self._pin, GPIO.OUT)

  def rotate(self, rotations):
    duration = datetime.timedelta(minute = self._rpm / rotations)
    GPIO.output(self._pin, False)
    time.sleep(duration.seconds)
    GPIO.output(self._pin, True)
