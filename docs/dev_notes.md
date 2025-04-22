Development Notes
This document contains notes on the design and development of the mytools project.
Design Decisions

Two Packages: The project is split into mytools and myutils to separate distinct functionality. mytools focuses on tool-like classes (Tool1, Tool2), while myutils provides utility classes (Utils1, Utils2).
Simple Implementation: Initial methods (foo1, foo2, bar1, bar2) print basic messages for demonstration. Future versions may add complex logic.
Src Layout: The src/ directory is used to isolate package code, following PyPA recommendations for clarity and to prevent import issues.

TODO

Add more methods to Tool1 and Utils1 for advanced functionality.
Integrate Sphinx for API documentation.
Add CI/CD pipeline for automated testing and PyPI deployment.

Notes

The project uses setuptools for packaging, compatible with PEP 517/518.
Tests are located in tests/, covering both mytools and myutils.
Examples are in examples/, excluded from the .whl package via MANIFEST.in.

