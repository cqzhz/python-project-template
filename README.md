MyTools
A Python package providing mytools and myutils packages with utility classes.
Installation
You can install mytools via pip:
pip install mytools

Usage
Using mytools
from mytools import Tool1, Tool2

# Create instances
tool1 = Tool1()
tool2 = Tool2()

# Call methods
tool1.foo1()  # Prints: helloworld1
tool2.foo2()  # Prints: helloworld2

Using myutils
from myutils import Utils1, Utils2

# Create instances
utils1 = Utils1()
utils2 = Utils2()

# Call methods
utils1.bar1()  # Prints: helloutils1
utils2.bar2()  # Prints: helloutils2

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
