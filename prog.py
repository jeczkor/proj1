#!/usr/bin/python

import unittest
import sys

#komentarz

class Tdd(unittest.TestCase):
    def test1(self):
	self.assertEqual(15,12)

if __name__ == '__main__':
	unittest.main()
