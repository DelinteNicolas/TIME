# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 21:19:22 2022

@author: DELINTE Nicolas
"""

from setuptools import setup

import TIME

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='TIME-python',
    version=TIME.__version__,
    description='Implementation of TIME',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DelinteNicolas/TIME',
    author='Nicolas Delinte',
    author_email='nicolas.delinte@uclouvain.be',
    license='GNU General Public License v3.0',
    packages=['TIME'],
    install_requires=['dipy',
                      'nibabel',
                      'numpy',
                      'scipy',
                      ],

    classifiers=['Development Status :: 3 - Alpha',
                 'Natural Language :: English',
                 'Programming Language :: Python'],
)
