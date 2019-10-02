#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import exercise

import unittest
from mock import patch #, Mock, MagicMock

class ExcerciseTest(unittest.TestCase):
    """ unit testing """
    def setup(self):
        """ init test """
        pass

    def tearDown(self):
        """ clear test """
        pass

    def test_funcA(self):
        res = exercise.funcA(4, 10, 6)
        self.assertEqual(res, 6, "el entero promedio de 4,5,6 es 6")

    def test_funcA2(self):
        res = exercise.funcA(8, 8, 8)
        self.assertEqual(res, 8, "el entero promedio de 8,8,8 es 8")


    def test_funcB(self):
        res = exercise.funcB([4,5,6])
        self.assertTupleEqual(res, (3, 15), "[4,5,6] son 3 elementos y suman 15")

    def test_funcB2(self):
        res = exercise.funcB([4,5,6,7])
        self.assertTupleEqual(res, (4, 22), "[4,5,6,7] son 4 elementos y suman 7")

    def test_funcC(self):
        res = exercise.funcC({'pedro':45, 'alberto':30, 'lucia': 55})
        self.assertListEqual(res, ['pedro', 'lucia'], "debe retornar la lista en orden")

    def test_funcC2(self):
        res = exercise.funcC({'a':40, 'b':20, 'c': 10, 'd':0})
        self.assertListEqual(res, ['b', 'a'], "debe retornar la lista en orden")

    def test_funcD(self):
        res = exercise.funcD("Hola mundo")
        self.assertEqual(res, "odnum aloH", "debe invertir el mensaje")

    def test_funcD(self):
        res = exercise.funcD("Hola mundo  cruel")
        self.assertEqual(res, "leurc  odnum aloH", "debe invertir el ,mensaje completo")


if __name__ == '__main__':
    unittest.main()
