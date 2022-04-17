import unittest

from catfeeder.cat_feeder import CatFeeder

class MockMotor():
  def __init__(self):
    self.rotations = 0.0

  def rotate(self, rotations):
    # Track the number of rotations that have been called.
    self.rotations += rotations

class MockCamera():
  def __init__(self):
    self.files = []

  def cap_image(self, file):
    # Track which image files have been written.
    self.files.append(file)

class TestCatFeeder(unittest.TestCase):
  default_config = {
    "capture_pause_secs": 0,
    "units_per_rotation": 6,
  }

  def test_degen_feed(self):
    mock_motor = MockMotor()
    mock_camera = MockCamera()
    feeder = CatFeeder(motor = mock_motor, camera = mock_camera, config = self.default_config)
    feeder.feed(0)
    self.assertAlmostEqual(mock_motor.rotations, 0.0, places = 6)
    self.assertEqual(len(mock_camera.files), 1)

  def test_multiple_feeds(self):
    mock_motor = MockMotor()
    mock_camera = MockCamera()
    feeder = CatFeeder(motor = mock_motor, camera = mock_camera, config = self.default_config)
    feeder.feed(1)
    feeder.feed(2)
    feeder.feed(1)
    self.assertAlmostEqual(mock_motor.rotations, 4/6, places = 6)
    self.assertEqual(len(mock_camera.files), 3)

  def test_custom_units(self):
    mock_motor = MockMotor()
    mock_camera = MockCamera()
    config = {
      "capture_pause_secs": 0,
      "units_per_rotation": 3,
    }
    feeder = CatFeeder(motor = mock_motor, camera = mock_camera, config = config)
    feeder.feed(0)
    feeder.feed(4)
    self.assertAlmostEqual(mock_motor.rotations, 4/3, places = 6)
    self.assertEqual(len(mock_camera.files), 2)

  def test_no_camera(self):
    mock_motor = MockMotor()
    feeder = CatFeeder(motor = mock_motor, config = self.default_config)
    feeder.feed(1)
    self.assertAlmostEqual(mock_motor.rotations, 1/6, places = 6)

if __name__ == '__main__':
    unittest.main()
