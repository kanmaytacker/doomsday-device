from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"

NAME = "doomsday"
VERSION = "0.1.0"
DESCRIPTION = "Dr. Strangelove"
URL = "https://github.com/kanmaytacker/doomsday-device"
REQUIRES_PYTHON = ">=3.6"

AUTHOR = "Tanmay Kacker"
AUTHOR_EMAIL = "tanmay@locus.sh"

DEPENDENCIES = [
    "fuckit == 4.8.1",
    "pytest-runner==5.2.0"
]

DEV_DEPENDENCIES = ["pre-commit==2.4.0"]

TEST_DEPENDENCIES = ["pytest==5.3.5"]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    url=URL,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    python_requires=REQUIRES_PYTHON,
    install_requires=DEPENDENCIES,
    tests_require=TEST_DEPENDENCIES,
    extras_require={"dev": DEV_DEPENDENCIES},
    entry_points={"console_scripts": ["develop=doomsday.main:run"]},
)
