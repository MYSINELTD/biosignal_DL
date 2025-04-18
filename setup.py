# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="biosignal_DL",
    version="0.1.0",
    description="A package for analysing different types of biological timeseries",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Jantine Broek",
    author_email="jantine@mysine.io",
    url="https://github.com/MYSINELTD/biosignal_DL",
    license=license,
    python_requires=">=3.10",
    # packages=find_packages(where="src"),
    # package_dir={"": "src"},
    install_requires=[
            "pandas",
            "matplotlib",
            "pyyaml",
            "numpy",
            "scikit-learn",
            "scipy",
            "seaborn",
            "statsmodels",
            "torch",
            "pathlib",
        ],
    zip_safe=False,
    include_package_data=True,
)
