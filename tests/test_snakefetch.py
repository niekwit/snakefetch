"""
Unit tests for the snakefetch module
"""

import os
import sys
import unittest

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from snakefetch import fetch_repo

class TestFetchRepo(unittest.TestCase):

    def test_divide_by_three(self):
        self.assertEqual(fetch_repo("https://github.com/niekwit/damid-seq",
                                    "v0.4.0",
                                    "/tmp",
                                    "config,workflow"), True)

if __name__ == '__main__':
    unittest.main()
