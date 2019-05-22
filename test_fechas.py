# -*- coding: utf-8 -*-

"""
@author: jqlaverde
"""

import unittest
import fechas

class PruebasFechas(unittest.TestCase):

    def test_instanciado(self):
        try:
            fecha = fechas.Fecha((2019, 5, 21))
        except NameError:
            raise AssertionError("La clase fecha no esta definida")
        return True

    def test_atributos_obligatorios(self):
        fecha = fechas.Fecha((2019, 5, 21))
        self.assertEqual(fecha.ano, 2019)
        self.assertEqual(fecha.mes, 5)
        self.assertEqual(fecha.dia, 21)

    def test_inicializacion_atributos_secundarios(self):
        fecha = fechas.Fecha((2019, 5, 21))
        self.assertEqual(fecha.hora, 0)
        self.assertEqual(fecha.minutos, 0)
        self.assertEqual(fecha.segundos, 0)

    def test_atributos_secundarios_ingresados(self):
        fecha = fechas.Fecha((2019, 5, 21, 19, 40, 46))
        self.assertEqual(fecha.hora, 19)
        self.assertEqual(fecha.minutos, 40)
        self.assertEqual(fecha.segundos, 46)



if __name__=='__main__':
    unittest.main()
