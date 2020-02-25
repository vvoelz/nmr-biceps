#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path
from io import open
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
import sys

# parse_requirements() returns generator of pip.req.InstallRequirement objects
# We need two seperate requirement files due to the failure to install all at once.
#install_reqs1 = parse_requirements('requirements1.txt', session=False)
#install_reqs2 = parse_requirements('requirements2.txt', session=False)
#
## reqs is a list of requirement
## e.g. ['django==1.5.1', 'mezzanine==1.4.6']
#reqs1 = [str(ir.req) for ir in install_reqs1]
#req_links1 = [str(ir.url) for ir in install_reqs1]
#
#reqs2 = [str(ir.req) for ir in install_reqs2]
#req_links2 = [str(ir.url) for ir in install_reqs2]

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

sys.path.append('BICePs_2.0/')

setup(
        name="biceps",
        version="2.0",
        description='BICePs',
        long_description=long_description,
        long_description_content_type="text/markdown",
        classifiers=[
        #'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Bio-Informatics'],
        url="https://biceps.readthedocs.io/en/latest/index.html",
            project_urls={
                "Github": "https://github.com/vvoelz/biceps",
                "Documentation": "https://biceps.readthedocs.io/en/latest/index.html",
            },
        author='Yunhui Ge, Robert M. Raddi, Vincent A. Voelz',
        author_email='vvoelz@gmail.com',
        license='MIT',
        #packages=exclude=['docs']),
        install_requires=[
            'numpy>=1.7.0','mdtraj==1.9.3','pymbar'],
        python_requires='>=3.6',
        #extras_require={  # Optional
        #        'dev': ['check-manifest'],
        #        'test': ['coverage'],
        #    },
        #dependency_links=req_links2,
        include_package_data=True,
        zip_safe=True)



