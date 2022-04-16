from setuptools import setup, find_packages

setup(
  name = "catfeeder",
  version = "0.1",
  packages = ['catfeeder'],
  entry_points={
    'console_scripts': [
      'feed-cats=catfeeder.cli:main',
    ],
  },
)

