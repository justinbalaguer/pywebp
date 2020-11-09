from setuptools import setup
setup(
  name = 'pywebp',
  version = '1.0.1',
  packages = ['pywebp'],
  entry_points = {
      'console_scripts': [
          'pywebp = pywebp.__main__:main'
      ]
  })