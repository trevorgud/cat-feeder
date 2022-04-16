from camera import Camera
from cat_feeder import CatFeeder
from rpi_motor import PiGpioMotor
import argparse
import picamera as picam

def main():
  args = parse_args()

  # TODO: Load a config file for some params.
  motor = PiGpioMotor(pin = 16, rpm = 9)

  hwcam = picam.PiCamera()
  hwcam.resolution = (1920, 1080)
  camera = Camera(hwcam)

  feeder = CatFeeder(motor = motor, camera = camera)
  feeder.feed(units = args.units)

def parse_args():
  parser = argparse.ArgumentParser(description = 'Parse cat feeder args')
  parser.add_argument(
    '--units',
    destintation = 'units',
    type = int,
    default = 1,
    help = 'how many units of food to dispense',
  )
  args = parser.parse_args()
  return args

if __name__ == '__main__':
  main()
