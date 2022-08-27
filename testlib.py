import libcplx as lc
import unittest
# Cristian David Naranjo
# Las funciones de modulo y fase no pude hacerle el test


class TestCplxoperations(unittest.TestCase):

    def test_Cplxsumacplx(self):
        suma = lc.sumacplx((2, 3), (4, 7))
        self.assertAlmostEqual(suma[0],6)
        self.assertAlmostEqual(suma[1],10)
    def test_restcplx(self):
        resta = lc.restcplx((2, 3), (4, 7))
        self.assertAlmostEqual(resta[0],-2)
        self.assertAlmostEqual(resta[1],-4)
    def test_multcplx(self):
        mult = lc.multcplx((3, -2), (1, 2))
        self.assertAlmostEqual(mult[0],7)
        self.assertAlmostEqual(mult[1],4)
    def test_divcplx(self):
        div = lc.divcplx((-2, 1), (1, 2))
        self.assertAlmostEqual(div[0],0)
        self.assertAlmostEqual(div[1],1)
    def test_modulo(self):
        modulo = lc.modulo((2, 2))
        print(modulo)
        self.assertAlmostEqual(modulo[0],2)
    def test_conjugado(self):
        conj = lc.conjugado(((3,3)))
        self.assertAlmostEqual(conj[0],3)
        self.assertAlmostEqual(conj[1],-3)
    def test_topolar(self):
        polar = lc.toPolar(((-3,-2)))
        self.assertAlmostEqual(polar[0],3.6)
        self.assertAlmostEqual(polar[1],-2.5)

    def test_tocartesian(self):
        cartesian = lc.toCartesian(((90, 4)))
        self.assertAlmostEqual(cartesian[0], -58.8)
        self.assertAlmostEqual(cartesian[1], -68.1)
    def test_Phase(self):
        phase = lc.Phase(((4,2)))
        print(phase)
        self.assertAlmostEqual(phase[0],0.9)
        



if __name__ == '__main__':
    unittest.main()