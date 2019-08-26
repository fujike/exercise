from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    author="KF",
    description="exercise output",
    python_requires='>=3.0',
    packages=find_packages(),
    entry_points={
           'console_scripts': ['myApp=src.main:main']
    },
)


