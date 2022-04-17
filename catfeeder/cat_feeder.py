from datetime import datetime
import logging
import time

_DEFAULT_UNITS_PER_ROTATION = 6
_DEFAULT_CAPTURE_PAUSE_SECS = 3
_DEFAULT_IMAGE_PREFIX = "fed-"
_DEFAULT_IMAGE_EXT = ".jpg"

class CatFeeder():
  def __init__(self, motor, camera = None, config = {}):
    self._logger = logging.getLogger(self.__class__.__name__)
    self._motor = motor
    self._camera = camera
    self._config = config

  # Feed (dispense) the given number of units from the feeder.
  def feed(self, units):
    rotations = units / self._units_per_rotation()
    self._logger.info(f'Feeding {units} units ({rotations} rotations)...')
    self._motor.rotate(rotations)
    # Pause for feeding to complete.
    time.sleep(self._capture_pause_secs())
    self._camera_capture()
    self._logger.info(f'Fed {units} units')

  def _camera_capture(self):
    if self._camera is None:
      return
    ts = datetime.now().strftime("%Y%m%dT%H%M%S")
    img_name = _DEFAULT_IMAGE_PREFIX + ts + _DEFAULT_IMAGE_EXT
    self._camera.cap_image(img_name)

  # How many units would be dispensed for a single full motor rotation.
  def _units_per_rotation(self):
    upr = self._config.get("units_per_rotation")
    if upr is None:
      upr = _DEFAULT_UNITS_PER_ROTATION
    return upr

  def _capture_pause_secs(self):
    pause = self._config.get("capture_pause_secs")
    if pause is None:
      pause = _DEFAULT_CAPTURE_PAUSE_SECS
    return pause
