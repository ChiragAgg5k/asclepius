import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.1"
DESCRIPTION = "Medicine Management System"
LONG_DESCRIPTION = (
    "A package that allows you to create a medicine management system"
)

# Setting up
setup(
    name="asclepius",
    version=VERSION,
    author="Chirag Aggarwal",
    author_email="<chiragaggarwal5k@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["customtkinter", "black", "Pillow"],
    keywords=[
        "python",
        "asclepius",
        "medicine",
        "dashboard",
        "custom tkinter",
        "management system",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
