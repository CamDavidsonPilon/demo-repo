#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='demorepo-cdp',
      version='0.0.1',
      description='demo',
      author='Cam Davidson-pilon',
      author_email='cam.davidson.pilon@gmail.com',
      url='https://github.com/CamDavidsonPilon/demo-repo',
      packages=['demo-repo'],
      long_description=read('README.md'),
      classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3",
        ],
      license="MIT",
)
