import RPi.GPIO as GPIO
import datetime
import time

class PiGpioMotor():
  def __init__(self, pin, rpm):
    self._rpm = rpm
    self._pin = pin
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self._pin, GPIO.OUT)

  def rotate(self, rotations):
    duration = datetime.timedelta(minutes = rotations / self._rpm)
    GPIO.output(self._pin, False)
    time.sleep(duration.total_seconds())
    GPIO.output(self._pin, True)

  def stop(self):
    GPIO.output(self._pin, True)
