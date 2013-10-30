#! /usr/bin/env python
import os
from setuptools import setup, find_packages

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='djpl-admintests',
    version='0.1',
    description='Django Productline Admin View Tests',
    license='The MIT License',
    keywords='django, django-productline, admin, views, test,',
    author='Michael Galler',
    author_email='michael@schnapptack.de',
    url="https://github.com/mgaller/djpl-admintests",
    packages=find_packages(),
    package_dir={'admintests': 'admintests'},
    include_package_data=True,
    scripts=[],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'django-productline',
    ]
)
