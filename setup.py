#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':
    setup(name='cimpy',
          version='0.9',
        description='Python package for import, modification and export of CIM grid data',
        author='Institute for Automation of Complex Power Systems',
        author_email='acs-software@eonerc.rwth-aachen.de',
        install_requires = [
            'lxml',
            'xmltodict',
            'chevron',
            'sphinx',
            'sphinx_rtd_theme',
        ]
     )
