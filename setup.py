#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

from setuptools import find_packages
from setuptools import setup

setup(
    name='microhackaton-python-deploy-service',
    version='0.0.1',
    description='A python service to deploy pthon microservices for http://microhackaton.github.io/2014/',
    author="Kamil Chmielewski",
    author_email='kamil.chm@gmail.com',
    url='https://github.com/microhackaton/python-deploy-service',
    license="ASL 2.0",
    install_requires=[
        'flask',
        'ansible',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
    ],
    keywords="deploy service ansible",
    packages=find_packages(),
    long_description=open("README.rst", "r").read(),
)
