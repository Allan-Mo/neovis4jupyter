# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pip._internal.req import parse_requirements

try:
    requirements = [str(ir.req) for ir in parse_requirements('requirements.txt', session=False)]
except:
    requirements = [str(ir.requirement) for ir in parse_requirements('requirements.txt', session=False)]

setup(
    name='neovis4jupyter',
    version='0.1',
    description='A tool to visualize graph database queries from Neo4j in the Jupyter Notebook, when you CANNOT access databases by javascript-driver, but CAN access from jupyter server.',
    packages=find_packages(),
    author='Allan Mo',
    author_email='moyunzheng@gmail.com',
    license='Apache License',
    package_data={'':['*','*/*','*/*/*','*/*/*/*','*/*/*/*/*','*/*/*/*/*/*','*/*/*/*/*/*/*']},
    url='https://github.com/Allan-Mo/neovis4jupyter',
    long_description='no_description',
    long_description_content_type='text/markdown',
    install_requires=requirements,
    zip_safe=False,
    platforms=['all'],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Operating System :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    python_requires='>=3.6'
)
