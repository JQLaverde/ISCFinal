# -*- coding: utf-8 -*-

"""
@author: jqlaverde
"""

class Fecha():
    """
    Clase de fecha en el calendario Gregoriano
    Entradas:
        fecha = (ano, mes, dia, hora, minutos, segundos)
    Atributos:
        ano: cualquier valor entero
        mes: natural entre 1 y 12
        dia: natural entre 1 y el numero de dias del mes
        hora: natural entre 0 y 23, por defecto es 0
        minutos: natural entre 0 y 59, por defecto es 0
        segundos: natural entre 0 y 59, por defecto es 0
    """

    def __init__(self, fecha):
        self.__numeroDiasMes = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        self.ano = fecha[0]

        if fecha[1] < 1 or fecha[1] > 12:
            raise ValueError("El mes debe estar entre 1 y 12")
        self.mes = fecha[1]

        if fecha[2] < 1 or fecha[2] > self.__numeroDiasMes[self.mes]:
            raise ValueError("El dia debe estar entre 1 y %d"\
                            %(self.__numeroDiasMes[self.mes]))
        self.dia = fecha[2]

        if len(fecha) == 3:
            self.hora = 0
            self.minutos = 0
            self.segundos = 0
        elif len(fecha) == 6:

            if fecha[3] < 0 or fecha[3] > 23:
                raise ValueError("La hora debe estar entre 0 y 23")
            self.hora = fecha[3]

            if fecha[4] < 0 or fecha[4] > 59:
                raise ValueError("Los minutos debe estar entre 0 y 59")
            self.minutos = fecha[4]

            if fecha[5] < 0 or fecha[5] > 59:
                raise ValueError("Los segundos debe estar entre 0 y 59")
            self.segundos = fecha[5]

    def __eq__(self, fechaCompara):
        if self.ano == fechaCompara.ano and\
           self.mes == fechaCompara.mes and\
           self.dia == fechaCompara.dia and\
           self.hora == fechaCompara.hora and\
           self.minutos == fechaCompara.minutos and\
           self.segundos == fechaCompara.segundos:
           return True

        return False

    def sumarAnos(self, numeroAnos):
        fechaNueva = Fecha((self.ano, self.mes, self.dia))
        fechaNueva.ano += numeroAnos
        return fechaNueva

    def sumarMeses(self, numeroMeses):
        fechaNueva = Fecha((self.ano, self.mes, self.dia))
        fechaNueva.mes += numeroMeses

        while fechaNueva.mes > 12:
            fechaNueva.mes -= 12
            fechaNueva.ano += 1

        return fechaNueva
