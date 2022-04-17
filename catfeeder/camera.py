import time

class Camera():
  def __init__(self, camera):
    self._camera = camera
    self._warmup()

  def cap_image(self, file):
    self._camera.capture(file)

  def cap_video(self, file, duration):
    pass
    # TODO: Implement

  def _warmup(self):
    self._camera.start_preview()
    time.sleep(2)
