#-------------------------------------------------------------------------------
# This file is part of PyMad.
#
# Copyright (c) 2011, CERN. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#-------------------------------------------------------------------------------
from setuptools import setup


# Compose a long description for PyPI
long_description = None
try:
    long_description = open('README.rst').read()
    long_description += '\n' + open('CHANGES.rst').read()
except IOError:
    pass

setup(
    name='cern-jpymad',
    version='0.5',
    description='Interface to Mad-X, using Py4J through JMAD',
    long_description=long_description,
    url='http://cern.ch/pymad',
    package_dir={'':'src'},
    packages = [
        "cern",
        "cern.jpymad",
        "cern.jpymad.tools",
    ],
    install_requires=['numpy', 'py4j'],
    author='PyMAD developers',
    author_email='pymad@cern.ch',
    license='CERN Standard Copyright License',
    zip_safe=True,
)

