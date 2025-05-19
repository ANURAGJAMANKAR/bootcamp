"""
Include Extra Files

Instructions:
Complete the exercise according to the requirements.
"""

# Author: ANURAG
# Include additional files (e.g., data files, configurations) in the distribution

[tool.setuptools.package_data]
mypkg = ["data/*.txt", "config/*.yaml"]

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
