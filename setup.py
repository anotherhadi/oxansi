from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'A Handy Python package to Use ANSI Escape Sequences'
LONG_DESCRIPTION = 'A handy package to use ansi escape sequences without having to know all possible sequences by heart'

# Setting up
setup(
    name="oxansi",
    version=VERSION,
    author="0x68616469",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['ansi', 'sequence'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)