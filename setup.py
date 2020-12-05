#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    name='shelter',
    version='0.0.1',
    author='Jason C. McDonald',
    author_email='codemouse92@outlook.com',

    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude=('tests')),
    include_package_data=True,
    python_requires='>=3.6, <4',
    install_requires=[],

    entry_points={
        'console_scripts': [
            'shelter=shelter.__main__:main'
        ]
    }
)
