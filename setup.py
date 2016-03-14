# coding=utf-8
from setuptools import setup

setup(
    name='data-structures',
    description='data-structures',
    version=0.1,
    author='Joe McClenahan and Alex German',
    author_email='jmcclena94@gmail.com alexgerman11233@gmail.com',
    license='MIT',
    py_modules=['client'],
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},
)
