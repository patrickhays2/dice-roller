#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
	name='your-package-name',  # Replace with your desired package name
	version='0.1',            # Start with a version number like 0.1
	packages=find_packages(),  # Automatically find all packages in your project
	install_requires=[         # List any dependencies your package needs
		# e.g., 'requests', 'numpy'
	],
)