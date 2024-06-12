from unittest import TestCase

from calc import Calc


class TestCalc(TestCase):
    def test_get_sum_sum(self):
        calc = Calc()

        expected = calc.getSumSum(1,2,3)

        actual = 6
        self.assertEqual(expected, actual)

