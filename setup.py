from setuptools import setup, find_packages
import os
import io

VERSION = "0.0.0a1"


def get_long_description():
    with io.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="kiwidb",
    description="Small in-memory, key-value database.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Ernesto González",
    version=VERSION,
    license="Apache License, Version 2.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "click-default-group>=1.2.3",
    ],
    url="https://github.com/ernestofgonzalez/kiwidb",
    project_urls={
        "Source code": "https://github.com/ernestofgonzalez/kiwidb",
        "Issues": "https://github.com/ernestofgonzalez/kiwidb/issues",
        "CI": "https://github.com/ernestofgonzalez/kiwidb/actions",
    },
    python_requires=">=3.10",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)