#!/usr/bin/env python3.8


try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup


setup(name='zet',
      version='0.0.1',
      description='zet',
      url='https://github.com/inconvergent/zet',
      license='MIT License',
      author='Anders Hoff',
      author_email='inconvergent@gmail.com',
      install_requires=['docopt', 'requests'],
      packages=['zet'],
      entry_points={'console_scripts': ['zet=zet:main']},
      zip_safe=True,
      )

