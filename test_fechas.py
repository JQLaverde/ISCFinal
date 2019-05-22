# -*- coding: utf-8 -*-

"""
@author: jqlaverde
"""

import unittest
import fechas

class PruebasFechas(unittest.TestCase):

    def test_instanciado(self):
        try:
            fechas.Fecha((2019, 5, 21))
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

    def test_rango_mes(self):
        try:
            fechas.Fecha((2019, 13, 5))
        except ValueError:
            return True
        raise AssertionError("No esta verificando el mes")

    def test_numeros_dias_meses(self):
        fecha = fechas.Fecha((2019, 3, 5))
        self.assertEqual(fecha._Fecha__numeroDiasMes[1], 31)
        self.assertEqual(fecha._Fecha__numeroDiasMes[2], 28)
        self.assertEqual(fecha._Fecha__numeroDiasMes[3], 31)
        self.assertEqual(fecha._Fecha__numeroDiasMes[4], 30)
        self.assertEqual(fecha._Fecha__numeroDiasMes[5], 31)
        self.assertEqual(fecha._Fecha__numeroDiasMes[6], 30)
        self.assertEqual(fecha._Fecha__numeroDiasMes[7], 31)
        self.assertEqual(fecha._Fecha__numeroDiasMes[8], 31)
        self.assertEqual(fecha._Fecha__numeroDiasMes[9], 30)
        self.assertEqual(fecha._Fecha__numeroDiasMes[10], 31)
        self.assertEqual(fecha._Fecha__numeroDiasMes[11], 30)
        self.assertEqual(fecha._Fecha__numeroDiasMes[12], 31)

    def test_rango_dia(self):
        for mes in range(1, 13):
            try:
                fechaAux = fechas.Fecha((2019, 3, 5))
                fechas.Fecha((2019, mes, fechaAux._Fecha__numeroDiasMes[mes] + 1))
            except ValueError:
                continue
            raise AssertionError("No esta verificando el dia")

    def test_rango_hora(self):
        try:
            fechas.Fecha((2019, 3, 5, 24, 0, 0))
        except ValueError:
            return True
        raise AssertionError("No esta verificando la hora")

    def test_rango_minutos(self):
        try:
            fechas.Fecha((2019, 3, 5, 23, 60, 0))
        except ValueError:
            return True
        raise AssertionError("No esta verificando los minutos")

    def test_rango_segundos(self):
        try:
            fechas.Fecha((2019, 3, 5, 23, 10, 60))
        except ValueError:
            return True
        raise AssertionError("No esta verificando los segundos")

    def test_compara_fechas(self):
        fechaInicial = fechas.Fecha((2019, 3, 5, 5, 5, 5))
        fechaCompara = fechas.Fecha((2019, 3, 5, 5, 5, 5))
        self.assertTrue(fechaInicial == fechaCompara)

    def test_suma_anos(self):
        fecha = fechas.Fecha((2019, 5, 19))
        fechaNueva = fecha.sumarAnos(1)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 5, 19)))

    def test_sumar_pocos_meses(self):
        fecha = fechas.Fecha((2019, 5, 19))
        fechaNueva = fecha.sumarMeses(4)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 9, 19)))

    def test_sumar_meses_pasando_ano(self):
        fecha = fechas.Fecha((2019, 5, 19))
        fechaNueva = fecha.sumarMeses(12)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 5, 19)))

    def test_sumar_meses_pasando_anos(self):
        fecha = fechas.Fecha((2019, 5, 19))
        fechaNueva = fecha.sumarMeses(27)
        self.assertTrue(fechaNueva == fechas.Fecha((2021, 8, 19)))

    

if __name__=='__main__':
    unittest.main()
