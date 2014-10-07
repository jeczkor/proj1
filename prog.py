#!/usr/bin/python

import unittest
import sys

class Tdd(unittest.TestCase):
    def test1(self):
	self.assertEqual(13,12)

if __name__ == '__main__':
	unittest.main()
