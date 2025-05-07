"""
Minimal Project File

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG
# This is the pyproject.toml file used for configuring the project metadata and build system.

[project]
name = "mypkg"
version = "0.1.0"
description = "A sample Python package"
authors = [
    { name = "ANURAG", email = "your-email@example.com" }
]
dependencies = ["requests"]

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

# Optional metadata for your project
license = { text = "MIT" }
