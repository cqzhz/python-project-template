MyTools
A Python package providing mytools and myutils packages with utility classes.
Installation
You can install mytools via pip:
pip install mytools

Usage
Using mytools
from mytools import Tool1, Tool2

tool1 = Tool1()
tool2 = Tool2()

tool1.foo1()  # Prints: helloworld1
tool2.foo2()  # Prints: helloworld2

Using myutils
from myutils import Utils1, Utils2

utils1 = Utils1()
utils2 = Utils2()

utils1.bar1()  # Prints: helloutils1
utils2.bar2()  # Prints: helloutils2

For more examples, see the examples/ directory, particularly use_tools_and_utils.py.
Documentation
Detailed documentation is available in the docs/ directory:

User Guide: How to use the packages.
Development Notes: Design decisions and TODOs.
Changelog: Version history.

Development
To set up the development environment:

Clone the repository:
git clone https://github.com/yourusername/mytools.git
cd mytools


Install dependencies:
pip install -e .[dev]


Run tests:
python -m unittest discover tests



License
This project is licensed under the MIT License. See the LICENSE file for details.
