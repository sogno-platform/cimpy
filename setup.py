#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':
    setup(name='cimpy',
          version='0.1',
          description='Python CIM Utilities',
          author='Institute for Automation of Complex Power Systems',
          author_email='acs-software@eonerc.rwth-aachen.de',
          include_package_data=True,
          install_requires=[
            'lxml',
            'xmltodict',
            'chevron',
        ]
     )
