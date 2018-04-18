#!/usr/bin/env python3
import num
import unittest


class MyTestCase(unittest.TestCase):

    def test_adding(self):
        res = num.Num(2).plus(num.Num(3))
        self.assertEqual(num.Num(5), res, "2 + 3 peaks olema 5")

    def test_repr(self):
        res = num.Num(-4).__repr__()
        self.assertEqual("Num(-4)", res, "kontrollida __repr__ meetodit")

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError, msg="nulliga jagamine peaks olema viga"):
            num.Num(3).divide_by(num.Num(0))


if __name__ == '__main__':
    unittest.main()

