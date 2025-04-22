import unittest
from src.mytools import Tool1, Tool2

class TestTools(unittest.TestCase):
    def test_tool1_foo1(self):
        tool1 = Tool1()
        with captured_output() as (out, err):
            tool1.foo1()
        self.assertEqual(out.getvalue().strip(), "helloworld1")

    def test_tool2_foo2(self):
        tool2 = Tool2()
        with captured_output() as (out, err):
            tool2.foo2()
        self.assertEqual(out.getvalue().strip(), "helloworld2")

from contextlib import contextmanager
from io import StringIO
import sys

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

if __name__ == "__main__":
    unittest.main()