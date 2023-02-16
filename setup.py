# pylint: disable=invalid-name, exec-used
"""Setup sonyapilib package."""
from __future__ import absolute_import

import os
import sys

from setuptools import setup

sys.path.insert(0, '.')

CURRENT_DIR = os.path.dirname(__file__)

# to deploy to pip, please use
# make pythonpack
# python setup.py register sdist upload
# and be sure to test it firstly using
# "python setup.py register sdist upload -r pypitest"
setup(
    name='sonyapilib',
    packages=['sonyapilib'],  # this must be the same as the name above
    version='1.1',
    description='Lib to control sony devices with their soap api',
    author='Leo',
    author_email='sonyapilib@xxxx',
    # use the URL to the github repo
    url='https://github.com/gohlas/APIlib-python-test',
    download_url='https://github.com/gohlas/APIlib-python-test/archive/1.1.tar.gz',
    keywords=['soap', 'sony', 'api'],  # arbitrary keywords
    classifiers=[],
    setup_requires=[
        'wheel'
    ],
    install_requires=[
        'jsonpickle',
        'setuptools',
        'requests',
        'wakeonlan'
    ],
    tests_require=[
        'pytest>=5.4',
        'pytest-pep8',
        'pytest-cov',
        'python-coveralls',
        'pylint',
        'coverage==4.5.4'
    ]
)
