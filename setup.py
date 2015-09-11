#!/usr/bin/env python

from setuptools import setup

setup(
    name='md5_pipeline',
    version='0.0.1',
    author='Bernie Pope',
    author_email='bjpope@unimelb.edu.au',
    packages=['src'],
    entry_points={
        'console_scripts': ['md5_pipeline = src.main:main']
    },
    url='https://github.com/bjpop/md5_pipeline',
    license='LICENSE.txt',
    description='md5_pipeline is a pipeline system for running md5 checksums\
     over many files on a distributed compute cluster.',
    long_description=open('README.md').read(),
    install_requires=[
        "ruffus == 2.6.3",
        "drmaa == 0.7.6",
        "PyYAML == 3.11"
    ],
)
