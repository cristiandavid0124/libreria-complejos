import libcplx as lc
import unittest


class TestCplxoperations(unittest.TestCase):

    def test_Cplxsumacplx(self):
        suma = lc.sumacplx((2, 3), (4, 7))
        self.assertEqual(suma[0],6)
        self.assertEqual(suma[1],10)


if __name__ == '__main__':
    unittest.main()