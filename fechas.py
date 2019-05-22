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

        self.ano = fecha[0]
        self.mes = fecha[1]
        self.dia = fecha[2]

        if len(fecha) == 3:
            self.hora = 0
            self.minutos = 0
            self.segundos = 0
        elif len(fecha) == 6:
            self.hora = fecha[3]
            self.minutos = fecha[4]
            self.segundos = fecha[5]
