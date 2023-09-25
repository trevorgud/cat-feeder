from catfeeder.camera import Camera
from catfeeder.cat_feeder import CatFeeder
from catfeeder.rpi_motor import PiGpioMotor
import argparse
import logging
import picamera as picam

def main():
  logging.basicConfig(level = logging.INFO)
  args = parse_args()

  # TODO: Load a config file for some params.
  motor = PiGpioMotor(pin = 16, rpm = 15)

  hwcam = picam.PiCamera()
  hwcam.resolution = (1920, 1080)
  camera = Camera(hwcam)

  feeder = CatFeeder(motor = motor, camera = camera)
  feeder.feed(units = args.units)

def parse_args():
  parser = argparse.ArgumentParser(description = 'Parse cat feeder args')
  parser.add_argument(
    '--units',
    dest = 'units',
    type = float,
    default = 1.0,
    help = 'how many units of food to dispense',
  )
  args = parser.parse_args()
  return args

if __name__ == '__main__':
  main()
