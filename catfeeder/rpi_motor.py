import RPi.GPIO as GPIO
import datetime
import time

# Duration of time motor continues to spin after deactivation.
MOTOR_LAG = datetime.timedelta(seconds = 0.25)

class PiGpioMotor():
  def __init__(self, pin, rpm):
    self._rpm = rpm
    self._pin = pin

  def rotate(self, rotations):
    duration = datetime.timedelta(minutes = rotations / self._rpm)
    if duration > MOTOR_LAG:
      duration = duration - MOTOR_LAG

    GPIO.setwarnings(False)
    GPIO.cleanup(self._pin)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self._pin, GPIO.OUT)
    GPIO.output(self._pin, GPIO.HIGH)
    GPIO.output(self._pin, GPIO.LOW)
    time.sleep(duration.total_seconds())
    GPIO.output(self._pin, GPIO.HIGH)
    GPIO.cleanup(self._pin)
