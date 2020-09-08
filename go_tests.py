#!/usr/bin/env python3
import os
import sys
import unittest


def main(pattern=None):
    """
    """
    suite = unittest.TestSuite()

    start_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests")
    args = [start_dir]
    if pattern:
        args.append("{}*".format(pattern))

    for test in unittest.TestLoader().discover(*args):
        suite.addTest(test)

    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    main(*sys.argv[1:])
