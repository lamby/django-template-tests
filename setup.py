#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-template-tests',

    url="https://chris-lamb.co.uk/projects/django-template-tests",
    version='1.0.0',
    description="Performs some quick static analysis on your templates",

    author="Chris Lamb",
    author_email="chris@chris-lamb.co.uk",
    license="BSD",

    packages=find_packages(),
    include_package_data=True,
)
