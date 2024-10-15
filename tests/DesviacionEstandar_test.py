import unittest
from unittest import TestCase
from src.logic.DesviacionEstandar import DesviaciónEstandar
class TestConjunto(TestCase):
    def test_conjunto_vacio_retornaNone(self):
        desviacion = DesviaciónEstandar([])
        self.assertIsNone(desviacion.calcular_desviacion())

if __name__ == '__main__':
    unittest.main()