# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='SDM',
    version='0.0.0b',
    description='Sequential Decision Making Library for General Learning',
    long_description=readme,
    author='Shotaro Ikeda & Akshay Mishra',
    author_email='ikeda2@illinois.edu',
    url='https://github.com/sig-ai/SDM',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
