"""
Image Palette Detector
-----------

Fast and accurate image RGB palette detector by Eugene Gourieff.

Links
`````

* `github <https://github.com/Gourieff/img-palette-detector'>`

"""

from setuptools import setup

setup(name='img-pd',
      version='0.2',
      description='Fast and accurate image RGB palette detector by Eugene Gourieff',
      url='https://github.com/Gourieff/img-palette-detector',
      author='Gourieff',
      author_email='gourieff@gmail.com',
      license='GPL-3.0',
      packages=['modules'],
      py_modules=['ipd'],
      install_requires=[
        'opencv-python',
        'colorthief',
        'argparse'
      ],
      zip_safe=False)