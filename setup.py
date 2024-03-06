from __future__ import annotations

import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

install_requires = (here / 'requirements-setup.txt').read_text(encoding='utf-8').splitlines()

setup(
    install_requires = install_requires,
    package_dir={'':'src'},
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'randnumber=tools_package.randnumber:main',
            'randnumber2=tools_package.randnumber2:main'
        ],
    },
)