# -*- coding: utf-8 -*-

"""
    setup.py
    ~~~~~~~~~~~~~~~~~~~~~

    Setup package infos.

    :author: qwezarty
    :date: 03:43 pm Nov 14 2017
    :email: qwezarty@gmail.com
"""

from setuptools import setup, find_packages

setup(
    name="wow-addon-manager",
    version="0.0.1",
    description="A cli tool for maintaining World of Warcraft addons.",
    license="MIT",

    url="https://github.com/qwezarty/wow-addon-manager",
    author="qwezarty",
    author_email="qwezarty@gmail.com",

    # packages=['wow-addon-manager'],
    # package_dir={'wow-addon-manager': 'wow-addon-manager'},
    # data_files=[('config', ['system.json', 'user.sample.json'])],
    packages=find_packages(),
    include_package_data=True,
    data_files = [
        ('wow_addon_manager/configs', ['system.json', 'user.sample.json'])
    ],
    platforms = "any",
    install_requires=["requests"],
    entry_points = {
        'console_scripts': [
            'wam = wow_addon_manager.cli:main',
            'wow_addon_manager = wow_addon_manager.cli:main',
        ]
    }
)
