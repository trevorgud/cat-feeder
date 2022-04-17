from catfeeder.rpi_motor import PiGpioMotor

def main():
  motor = PiGpioMotor(pin = 16, rpm = 25)
  # motor.stop()
  motor.rotate(1/3)

if __name__ == "__main__":
  main()
