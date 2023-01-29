"""
Image Palette Detector
-----------

Fast image RGB palette detector by Gourieff.

Links
`````

* `github <https://github.com/Gourieff/img-palette-detector'>`

"""

from setuptools import setup

setup(name='img-pd',
      version='0.1',
      description='Fast image RGB palette detector by Gourieff',
      url='https://github.com/Gourieff/img-palette-detector',
      author='Gourieff',
      author_email='gourieff@gmail.com',
      license='GPL-3.0',
      packages=['modules'],
      py_modules=['ipd'],
      install_requires=[
        'opencv-python',
        'colorthief'
      ],
      zip_safe=False)