#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pip.req import parse_requirements
from setuptools import find_packages, setup
import pydirstructure


install_reqs = parse_requirements('requirements.txt', session=False)


setup(
    name='pydirstructure',
    version=pydirstructure.__version__,
    description='Example project to show directory structure',
    author='Koen Dercksen',
    author_email='mail@koendercksen.com',
    url='http://github.com/KDercksen/pydirstructure',
    install_requires=[str(ir.req) for ir in install_reqs],
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'pydir_a=pydirstructure.module_a:main',
            'pydir_b=pydirstructure.module_b:main',
        ]
    }
)
