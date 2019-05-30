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

    def test_comprobar_cantidad_parametros(self):
        try:
            fechas.Fecha((2019, 5, 21, 23))
        except ValueError:
            return True
        raise AssertionError("No esta verificando parametros")

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

    def test_compara_fechas_true(self):
        fechaInicial = fechas.Fecha((2019, 3, 5, 5, 5, 5))
        fechaCompara = fechas.Fecha((2019, 3, 5, 5, 5, 5))
        self.assertTrue(fechaInicial == fechaCompara)

    def test_comparar_fechas_false(self):
        fechaInicial = fechas.Fecha((2019, 3, 5, 5, 5, 5))
        fechaCompara = fechas.Fecha((2019, 3, 5, 6, 5, 5))
        self.assertFalse(fechaInicial == fechaCompara)

    def test_sumar_anos(self):
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

    def test_sumar_pocos_dias(self):
        fecha = fechas.Fecha((2019, 5, 22))
        fechaNueva = fecha.sumarDias(5)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 5, 27)))

    def test_sumar_dias_pasando_mes(self):
        fecha = fechas.Fecha((2019, 5, 22))
        fechaNueva = fecha.sumarDias(15)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 6, 6)))

    def test_sumar_dias_pasando_meses(self):
        fecha = fechas.Fecha((2019, 5, 22))
        fechaNueva = fecha.sumarDias(45)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 7, 6)))

    def test_sumar_dias_pasando_anos(self):
        fecha = fechas.Fecha((2018, 5, 22))
        fechaNueva = fecha.sumarDias(365)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 5, 22)))

    def test_29_febrero(self):
        try:
            fechas.Fecha((2020, 2, 29))
        except ValueError:
            raise AssertionError("No esta reconociendo bisciestos")

    def test_sumar_dias_pasando_mes_ano_bisciesto(self):
        fecha = fechas.Fecha((2020, 2, 20))
        fechaNueva = fecha.sumarDias(20)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 3, 11)))

    def test_sumar_dias_pasando_ano_bisciesto(self):
        fecha = fechas.Fecha((2019, 3, 5))
        fechaNueva = fecha.sumarDias(365)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 3, 4)))

    def test_sumar_pocas_horas(self):
        fecha = fechas.Fecha((2019, 3, 5))
        fechaNueva = fecha.sumarHoras(10)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 10, 0, 0)))

    def test_sumar_horas_pasando_dia(self):
        fecha = fechas.Fecha((2019, 3, 5, 23, 0, 0))
        fechaNueva = fecha.sumarHoras(24)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 6, 23, 0, 0)))

    def test_sumar_horas_pasando_dias(self):
        fecha = fechas.Fecha((2019, 3, 5, 23, 0, 0))
        fechaNueva = fecha.sumarHoras(32)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 7, 7, 0, 0)))

    def test_sumar_horas_pasando_mes(self):
        fecha = fechas.Fecha((2019, 5, 22))
        fechaNueva = fecha.sumarHoras(245)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 6, 1, 5, 0, 0)))

    def test_sumar_horas_pasando_meses(self):
        fecha = fechas.Fecha((2019, 5, 22))
        fechaNueva = fecha.sumarHoras(984)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 7, 2, 0, 0, 0)))

    def test_sumar_horas_pasando_anos(self):
        fecha = fechas.Fecha((2019, 12, 27))
        fechaNueva = fecha.sumarHoras(120)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 1, 1, 0, 0, 0)))

    def test_sumar_horas_pasando_mes_ano_bisciesto(self):
        fecha = fechas.Fecha((2020, 2, 20))
        fechaNueva = fecha.sumarHoras(240)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 3, 1)))

    def test_suma_horas_pasando_ano_bisciesto(self):
        fecha = fechas.Fecha((2019, 12, 27))
        fechaNueva = fecha.sumarHoras(1560)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 3, 1)))

    def test_sumar_pocos_minutos(self):
        fecha = fechas.Fecha((2019, 3, 5))
        fechaNueva = fecha.sumarMinutos(10)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 10, 0)))

    def test_sumar_minutos_pasando_hora(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
        fechaNueva = fecha.sumarMinutos(61)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 1, 1, 0)))

    def test_sumar_minutos_pasando_horas(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
        fechaNueva = fecha.sumarMinutos(181)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 3, 1, 0)))

    def test_sumar_minutos_pasando_dia(self):
          fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
          fechaNueva = fecha.sumarMinutos(1441)
          self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 6, 0, 1, 0)))

    def test_sumar_minutos_pasando_dias(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
        fechaNueva = fecha.sumarMinutos(2881)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 7, 0, 1, 0)))

    def test_sumar_minutos_pasando_mes(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
        fechaNueva = fecha.sumarMinutos(44641)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 4, 5, 0, 1, 0)))

    def test_sumar_minutos_pasando_meses(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
        fechaNueva = fecha.sumarMinutos(89281)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 5, 6, 0, 1, 0)))

    def test_sumar_minutos_pasando_anos(self):
        fecha = fechas.Fecha((2019, 12, 27))
        fechaNueva = fecha.sumarMinutos(7201)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 1, 1, 0, 1, 0)))

    def test_sumar_minutos_pasando_mes_ano_bisciesto(self):
        fecha = fechas.Fecha((2020, 2, 20))
        fechaNueva = fecha.sumarMinutos(14401)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 3, 1, 0, 1, 0)))

    def test_sumar_minutos_pasando_ano_bisciesto(self):
        fecha = fechas.Fecha((2019, 12, 27))
        fechaNueva = fecha.sumarMinutos(93601)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 3, 1, 0, 1, 0)))

    def test_sumar_pocos_segundos(self):
        fecha = fechas.Fecha((2019, 3, 5))
        fechaNueva = fecha.sumarSegundos(10)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 10)))

    def test_sumar_segundos_pasando_minuto(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
        fechaNueva = fecha.sumarSegundos(61)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 1, 1)))

    def test_sumar_segundos_pasando_minutos(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
        fechaNueva = fecha.sumarSegundos(301)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 5, 1)))

    def test_sumar_segundos_pasando_hora(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
        fechaNueva = fecha.sumarSegundos(3601)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 1, 0, 1)))

    def test_sumar_segundos_pasando_horas(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
        fechaNueva = fecha.sumarSegundos(10801)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 3, 0, 1)))

    def test_sumar_segundos_pasando_dia(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
        fechaNueva = fecha.sumarSegundos(86401)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 6, 0, 0, 1)))

    def test_sumar_segundos_pasando_dias(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
        fechaNueva = fecha.sumarSegundos(172801)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 7, 0, 0, 1)))

    def test_sumar_segundos_pasando_mes(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
        fechaNueva = fecha.sumarSegundos(2678401)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 4, 5, 0, 0, 1)))

    def test_sumar_segundos_pasando_meses(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 0))
        fechaNueva = fecha.sumarSegundos(5356801)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 5, 6, 0, 0, 1)))

    def test_sumar_segundos_pasando_anos(self):
        fecha = fechas.Fecha((2019, 12, 27))
        fechaNueva = fecha.sumarSegundos(432001)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 1, 1, 0, 0, 1)))

    def test_sumar_segundos_pasando_mes_ano_bisciesto(self):
        fecha = fechas.Fecha((2020, 2, 20))
        fechaNueva = fecha.sumarSegundos(864001)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 3, 1, 0, 0, 1)))

    def test_suma_segundos_pasando_ano_bisciesto(self):
        fecha = fechas.Fecha((2019, 12, 27))
        fechaNueva = fecha.sumarSegundos(5616001)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 3, 1, 0, 0, 1)))

    def test_restar_anos(self):
        fecha = fechas.Fecha((2019, 5, 19))
        fechaNueva = fecha.restarAnos(1)
        self.assertTrue(fechaNueva == fechas.Fecha((2018, 5, 19)))

    def test_restar_pocos_meses(self):
        fecha = fechas.Fecha((2019, 5, 19))
        fechaNueva = fecha.restarMeses(4)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 1, 19)))

    def test_restar_meses_pasando_ano(self):
        fecha = fechas.Fecha((2019, 5, 19))
        fechaNueva = fecha.restarMeses(12)
        self.assertTrue(fechaNueva == fechas.Fecha((2018, 5, 19)))

    def test_restar_meses_pasando_anos(self):
        fecha = fechas.Fecha((2019, 5, 19))
        fechaNueva = fecha.restarMeses(27)
        self.assertTrue(fechaNueva == fechas.Fecha((2017, 2, 19)))

    def test_restar_pocos_dias(self):
        fecha = fechas.Fecha((2019, 5, 22))
        fechaNueva = fecha.restarDias(5)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 5, 17)))

    def test_restar_dias_pasando_mes(self):
        fecha = fechas.Fecha((2019, 5, 22))
        fechaNueva = fecha.restarDias(25)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 4, 27)))

    def test_restar_dias_pasando_meses(self):
        fecha = fechas.Fecha((2019, 5, 22))
        fechaNueva = fecha.restarDias(55)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 28)))

    def test_restar_dias_pasando_anos(self):
        fecha = fechas.Fecha((2019, 5, 22))
        fechaNueva = fecha.restarDias(365)
        self.assertTrue(fechaNueva == fechas.Fecha((2018, 5, 22)))

    def test_restar_dias_pasando_mes_ano_bisciesto(self):
        fecha = fechas.Fecha((2020, 3, 11))
        fechaNueva = fecha.restarDias(20)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 2, 20)))

    def test_restar_dias_pasando_ano_bisciesto(self):
        fecha = fechas.Fecha((2020, 3, 4))
        fechaNueva = fecha.restarDias(365)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5)))

    def test_restar_pocas_horas(self):
        fecha = fechas.Fecha((2019, 3, 5, 10, 0, 0))
        fechaNueva = fecha.restarHoras(10)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_horas_pasando_dia(self):
        fecha = fechas.Fecha((2019, 3, 6, 23, 0, 0))
        fechaNueva = fecha.restarHoras(24)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 23, 0, 0)))

    def test_restar_horas_pasando_dias(self):
        fecha = fechas.Fecha((2019, 3, 7, 7, 0, 0))
        fechaNueva = fecha.restarHoras(32)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 23, 0, 0)))

    def test_restar_horas_pasando_mes(self):
        fecha = fechas.Fecha((2019, 6, 1, 5, 0, 0))
        fechaNueva = fecha.restarHoras(245)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 5, 22, 0, 0, 0)))

    def test_restar_horas_pasando_meses(self):
        fecha = fechas.Fecha((2019, 7, 2, 0, 0, 0))
        fechaNueva = fecha.restarHoras(984)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 5, 22, 0, 0, 0)))

    def test_restar_horas_pasando_anos(self):
        fecha = fechas.Fecha((2020, 1, 1, 0, 0, 0))
        fechaNueva = fecha.restarHoras(120)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 12, 27, 0, 0, 0)))

    def test_restar_horas_pasando_mes_ano_bisciesto(self):
        fecha = fechas.Fecha((2020, 3, 1, 0, 0, 0))
        fechaNueva = fecha.restarHoras(240)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 2, 20, 0, 0, 0)))

    def test_restar_horas_pasando_ano_bisciesto(self):
        fecha = fechas.Fecha((2020, 3, 1, 0, 0, 0))
        fechaNueva = fecha.restarHoras(1560)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 12, 27, 0, 0, 0)))

    def test_restar_pocos_minutos(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 10, 0))
        fechaNueva = fecha.restarMinutos(10)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5)))

    def test_restar_minutos_pasando_hora(self):
        fecha = fechas.Fecha((2019, 3, 5, 1, 1, 0))
        fechaNueva = fecha.restarMinutos(61)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_minutos_pasando_horas(self):
        fecha = fechas.Fecha((2019, 3, 5, 3, 1, 0))
        fechaNueva = fecha.restarMinutos(181)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_minutos_pasando_dia(self):
          fecha = fechas.Fecha((2019, 3, 6, 0, 1, 0))
          fechaNueva = fecha.restarMinutos(1441)
          self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_minutos_pasando_dias(self):
        fecha = fechas.Fecha((2019, 3, 7, 0, 1, 0))
        fechaNueva = fecha.restarMinutos(2881)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_minutos_pasando_mes(self):
        fecha = fechas.Fecha((2019, 4, 5, 0, 1, 0))
        fechaNueva = fecha.restarMinutos(44641)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_minutos_pasando_meses(self):
        fecha = fechas.Fecha((2019, 5, 6, 0, 1, 0))
        fechaNueva = fecha.restarMinutos(89281)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_minutos_pasando_anos(self):
        fecha = fechas.Fecha((2020, 1, 1, 0, 1, 0))
        fechaNueva = fecha.restarMinutos(7201)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 12, 27)))

    def test_restar_minutos_pasando_mes_ano_bisciesto(self):
        fecha = fechas.Fecha((2020, 3, 1, 0, 1, 0))
        fechaNueva = fecha.restarMinutos(14401)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 2, 20)))

    def test_restar_minutos_pasando_ano_bisciesto(self):
        fecha = fechas.Fecha((2020, 3, 1, 0, 1, 0))
        fechaNueva = fecha.restarMinutos(93601)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 12, 27)))

    def test_restar_pocos_segundos(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 0, 10))
        fechaNueva = fecha.restarSegundos(10)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5)))

    def test_restar_segundos_pasando_minuto(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 1, 1))
        fechaNueva = fecha.restarSegundos(61)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_segundos_pasando_minutos(self):
        fecha = fechas.Fecha((2019, 3, 5, 0, 5, 1))
        fechaNueva = fecha.restarSegundos(301)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_segundos_pasando_hora(self):
        fecha = fechas.Fecha((2019, 3, 5, 1, 0, 1))
        fechaNueva = fecha.restarSegundos(3601)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_segundos_pasando_horas(self):
        fecha = fechas.Fecha((2019, 3, 5, 3, 0, 1))
        fechaNueva = fecha.restarSegundos(10801)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_segundos_pasando_dia(self):
        fecha = fechas.Fecha((2019, 3, 6, 0, 0, 1))
        fechaNueva = fecha.restarSegundos(86401)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_segundos_pasando_dias(self):
        fecha = fechas.Fecha((2019, 3, 7, 0, 0, 1))
        fechaNueva = fecha.restarSegundos(172801)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_segundos_pasando_mes(self):
        fecha = fechas.Fecha((2019, 4, 5, 0, 0, 1))
        fechaNueva = fecha.restarSegundos(2678401)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_segundos_pasando_meses(self):
        fecha = fechas.Fecha((2019, 5, 6, 0, 0, 1))
        fechaNueva = fecha.restarSegundos(5356801)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 3, 5, 0, 0, 0)))

    def test_restar_segundos_pasando_anos(self):
        fecha = fechas.Fecha((2020, 1, 1, 0, 0, 1))
        fechaNueva = fecha.restarSegundos(432001)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 12, 27)))

    def test_restar_segundos_pasando_mes_ano_bisciesto(self):
        fecha = fechas.Fecha((2020, 3, 1, 0, 0, 1))
        fechaNueva = fecha.restarSegundos(864001)
        self.assertTrue(fechaNueva == fechas.Fecha((2020, 2, 20)))

    def test_restar_segundos_pasando_ano_bisciesto(self):
        fecha = fechas.Fecha((2020, 3, 1, 0, 0, 1))
        fechaNueva = fecha.restarSegundos(5616001)
        self.assertTrue(fechaNueva == fechas.Fecha((2019, 12, 27)))

    def test_es_mas_reciente_ano(self):
        fechaInicial = fechas.Fecha((2019, 5, 29))
        fechaFinal = fechas.Fecha((2020, 3, 30))
        self.assertTrue(fechaFinal.esMasReciente(fechaInicial))

    def test_es_mas_reciente_mes(self):
        fechaInicial = fechas.Fecha((2019, 5, 29))
        fechaFinal = fechas.Fecha((2019, 8, 30))
        self.assertTrue(fechaFinal.esMasReciente(fechaInicial))

    def test_es_mas_reciente_dia(self):
        fechaInicial = fechas.Fecha((2019, 5, 29))
        fechaFinal = fechas.Fecha((2019, 5, 30))
        self.assertTrue(fechaFinal.esMasReciente(fechaInicial))

    def test_es_mas_reciente_hora(self):
        fechaInicial = fechas.Fecha((2019, 5, 29, 13, 13, 10))
        fechaFinal = fechas.Fecha((2019, 5, 29, 15, 13, 10))
        self.assertTrue(fechaFinal.esMasReciente(fechaInicial))

    def test_es_mas_reciente_minutos(self):
        fechaInicial = fechas.Fecha((2019, 5, 29, 15, 13, 10))
        fechaFinal = fechas.Fecha((2019, 5, 29, 15, 18, 10))
        self.assertTrue(fechaFinal.esMasReciente(fechaInicial))

    def test_es_mas_reciente_segundos(self):
        fechaInicial = fechas.Fecha((2019, 5, 29, 15, 18, 9))
        fechaFinal = fechas.Fecha((2019, 5, 29, 15, 18, 10))
        self.assertTrue(fechaFinal.esMasReciente(fechaInicial))

    def test_es_mas_reciente_fechas_iguales(self):
        fechaInicial = fechas.Fecha((2019, 5, 29, 15, 18, 10))
        fechaFinal = fechas.Fecha((2019, 5, 29, 15, 18, 10))
        self.assertFalse(fechaFinal.esMasReciente(fechaInicial))

    def test_distancia_dias_entre_fechas(self):
        fechaInicial = fechas.Fecha((2019, 5, 29))
        fechaFinal = fechas.Fecha((2019, 11, 30))
        distanciaDias = fechaInicial.calcularDistanciaEnDias(fechaFinal)
        self.assertEqual(distanciaDias, 185)

    def test_distancia_dias_entre_fechas_ano_desfase(self):
        fechaInicial = fechas.Fecha((1998, 8, 16))
        fechaFinal = fechas.Fecha((2019, 5, 29))
        distanciaDias = fechaInicial.calcularDistanciaEnDias(fechaFinal)
        self.assertEqual(distanciaDias, 7590)

    def test_distancia_dias_fechas_iguales(self):
        fechaInicial = fechas.Fecha((2019, 5, 29))
        fechaFinal = fechas.Fecha((2019, 5, 29))
        self.assertEqual(fechaInicial.calcularDistanciaEnDias(fechaFinal), 0)

    def test_distancia_dias_fechas_cambiar_orden(self):
        fechaInicial = fechas.Fecha((2019, 11, 30))
        fechaFinal = fechas.Fecha((2019, 5, 29))
        distanciaDias = fechaInicial.calcularDistanciaEnDias(fechaFinal)
        self.assertEqual(distanciaDias, 185)

    def test_restar_fechas(self):
        fechaFinal = fechas.Fecha((2020, 8, 16, 12, 3, 5))
        fechaInicial = fechas.Fecha((2019, 5, 29, 21, 9, 0))
        restaFechas = fechaFinal - fechaInicial
        self.assertEqual(restaFechas, fechas.Fecha((1, 3, 13, 9, 6, 5)))

    def test_restar_fechas_diferente_orden(self):
        fechaInicial = fechas.Fecha((2020, 8, 16, 12, 3, 5))
        fechaFinal = fechas.Fecha((2019, 5, 29, 21, 9, 0))
        restaFechas = fechaFinal - fechaInicial
        self.assertEqual(restaFechas, fechas.Fecha((1, 3, 13, 9, 6, 5)))

    def test_restar_fechas_meses_desfase(self):
        fechaInicial = fechas.Fecha((1998, 8, 16, 12, 3, 5))
        fechaFinal = fechas.Fecha((2019, 5, 29, 21, 9, 0))
        restaFechas = fechaFinal - fechaInicial
        self.assertEqual(restaFechas, fechas.Fecha((20, 9, 13, 9, 6, 5)))

    def test_instanciado_clase_hoy(self):
        try:
            fechas.Hoy()
        except NameError:
            raise AssertionError("La clase hoy no esta definida")
        return True

if __name__=='__main__':
    unittest.main()
    #print(fechaNueva.ano, fechaNueva.mes, fechaNueva.dia, fechaNueva.hora, fechaNueva.minutos, fechaNueva.segundos)
