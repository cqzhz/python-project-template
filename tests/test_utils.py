import unittest
from src.myutils import Utils1, Utils2

class TestUtils(unittest.TestCase):
    def test_utils1_bar1(self):
        utils1 = Utils1()
        with captured_output() as (out, err):
            utils1.bar1()
        self.assertEqual(out.getvalue().strip(), "helloutils1")

    def test_utils2_bar2(self):
        utils2 = Utils2()
        with captured_output() as (out, err):
            utils2.bar2()
        self.assertEqual(out.getvalue().strip(), "helloutils2")

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