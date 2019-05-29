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

    bisciesto = False

    def __init__(self, fecha):
        self.__numeroDiasMes = [None, 31, 28, 31, 30, 31, 30, \
                                      31, 31, 30, 31, 30, 31]
        self.ano = fecha[0]
        self.comprobarBisciesto()
        self.mes = self.comprobarRangoValor(fecha[1],
                                            [1, 12],
                                            "El mes debe estar entre 1 y 12")
        self.dia = self.comprobarRangoValor(fecha[2],
                                            [1, self.__numeroDiasMes[self.mes]],
                                            "El dia debe estar entre 1 y %d"\
                                            %(self.__numeroDiasMes[self.mes]))

        if len(fecha) == 3:
            self.hora = 0
            self.minutos = 0
            self.segundos = 0

        elif len(fecha) == 6:
            self.hora = self.comprobarRangoValor(fecha[3],
                                            [0, 23],
                                            "La hora debe estar entre 0 y 23")
            self.minutos = self.comprobarRangoValor(fecha[4],
                                        [0, 59],
                                        "Los minutos debe estar entre 0 y 59")
            self.segundos = self.comprobarRangoValor(fecha[5],
                                        [0, 59],
                                        "Los segundos debe estar entre 0 y 59")

        else:
            raise ValueError("Entrada debe ser (año, mes, dia)\
                                    o (año, mes, dia, hora, minutos, segundos)")

    def comprobarRangoValor(self, valor, limites, mensaje):
        if valor < limites[0] or valor > limites[1]:
            raise ValueError(mensaje)
        return valor

    def comprobarBisciesto(self):
        if (self.ano % 4) == 0 and (self.ano % 400) != 0 :
            self.__numeroDiasMes[2] = 29
            self.bisciesto = True
            return True

        self.__numeroDiasMes[2] = 28
        self.bisciesto = False
        return False

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
        fechaNueva = Fecha((self.ano, self.mes, self.dia,\
                            self.hora, self.minutos, self.segundos))
        fechaNueva.ano += numeroAnos
        fechaNueva.comprobarBisciesto()
        return fechaNueva

    def restarAnos(self, numeroAnos):
        fechaNueva = Fecha((self.ano, self.mes, self.dia,\
                            self.hora, self.minutos, self.segundos))
        fechaNueva.ano -= numeroAnos
        fechaNueva.comprobarBisciesto()
        return fechaNueva

    def sumarMeses(self, numeroMeses):
        fechaNueva = Fecha((self.ano, self.mes, self.dia,\
                            self.hora, self.minutos, self.segundos))
        fechaNueva.mes += numeroMeses

        while fechaNueva.mes > 12:
            fechaNueva.mes -= 12
            fechaNueva.ano += 1
            fechaNueva.comprobarBisciesto()

        return fechaNueva

    def restarMeses(self, numeroMeses):
        fechaNueva = Fecha((self.ano, self.mes, self.dia,\
                            self.hora, self.minutos, self.segundos))
        fechaNueva.mes -= numeroMeses

        while fechaNueva.mes < 1:
            fechaNueva.mes += 12
            fechaNueva.ano -= 1
            fechaNueva.comprobarBisciesto()

        return fechaNueva

    def aumentarAnoMes(self):
        if self.mes > 12:
            self.mes = 1
            self.ano += 1
            self.comprobarBisciesto()

    def disminuirAnoMes(self):
        if self.mes < 1:
            self.mes = 12
            self.ano -= 1
            self.comprobarBisciesto()

    def aumentarMesDia(self, numeroDiasMesActual):
        if self.dia > numeroDiasMesActual:
            self.dia -= numeroDiasMesActual
            self.mes += 1

    def disminuirAnoMesPorDias(self):
        if self.dia < 1:
            self.mes -= 1
            self.disminuirAnoMes()
            numeroDiasMesActual = self.__numeroDiasMes[self.mes]
            self.dia += numeroDiasMesActual

    def aumentarDiaHora(self):
        if self.hora > 23:
            self.hora -= 24
            self.dia += 1

    def disminuirDiaHora(self):
        if self.hora < 0:
            self.hora += 24
            self.dia -= 1

    def aumentarHoraMinutos(self):
        if self.minutos > 59:
            self.minutos -= 60
            self.hora += 1

    def disminuirHoraMinutos(self):
        if self.minutos < 0:
            self.minutos += 60
            self.hora -= 1

    def sumarDias(self, numeroDias):
        fechaNueva = Fecha((self.ano, self.mes, self.dia,
                            self.hora, self.minutos, self.segundos))
        fechaNueva.dia += numeroDias
        numeroDiasMesActual = fechaNueva.__numeroDiasMes[fechaNueva.mes]

        while fechaNueva.dia > numeroDiasMesActual:
            fechaNueva.dia -= numeroDiasMesActual
            fechaNueva.mes += 1
            fechaNueva.aumentarAnoMes()
            numeroDiasMesActual = fechaNueva.__numeroDiasMes[fechaNueva.mes]

        return fechaNueva

    def restarDias(self, numeroDias):
        fechaNueva = Fecha((self.ano, self.mes, self.dia,
                            self.hora, self.minutos, self.segundos))
        fechaNueva.dia -= numeroDias

        while fechaNueva.dia < 1:
            fechaNueva.mes -= 1
            fechaNueva.disminuirAnoMes()
            numeroDiasMesActual = fechaNueva.__numeroDiasMes[fechaNueva.mes]
            fechaNueva.dia += numeroDiasMesActual

        return fechaNueva

    def sumarHoras(self, numeroHoras):
        fechaNueva = Fecha((self.ano, self.mes, self.dia,
                            self.hora, self.minutos, self.segundos))
        fechaNueva.hora += numeroHoras
        numeroDiasMesActual = fechaNueva.__numeroDiasMes[fechaNueva.mes]

        while fechaNueva.hora > 23:
            fechaNueva.hora -= 24
            fechaNueva.dia += 1
            fechaNueva.aumentarMesDia(numeroDiasMesActual)
            fechaNueva.aumentarAnoMes()
            numeroDiasMesActual = fechaNueva.__numeroDiasMes[fechaNueva.mes]

        return fechaNueva

    def restarHoras(self, numeroHoras):
        fechaNueva = Fecha((self.ano, self.mes, self.dia,
                            self.hora, self.minutos, self.segundos))
        fechaNueva.hora -= numeroHoras

        while fechaNueva.hora < 0:
            fechaNueva.dia -= 1
            fechaNueva.disminuirAnoMesPorDias()
            fechaNueva.hora += 24

        return fechaNueva

    def sumarMinutos(self, numeroMinutos):
        fechaNueva = Fecha((self.ano, self.mes, self.dia,
                            self.hora, self.minutos, self.segundos))
        fechaNueva.minutos += numeroMinutos
        numeroDiasMesActual = fechaNueva.__numeroDiasMes[fechaNueva.mes]

        while fechaNueva.minutos > 59:
            fechaNueva.minutos -= 60
            fechaNueva.hora += 1
            fechaNueva.aumentarDiaHora()
            fechaNueva.aumentarMesDia(numeroDiasMesActual)
            fechaNueva.aumentarAnoMes()
            numeroDiasMesActual = fechaNueva.__numeroDiasMes[fechaNueva.mes]

        return fechaNueva

    def restarMinutos(self, numeroMinutos):
        fechaNueva = Fecha((self.ano, self.mes, self.dia,
                            self.hora, self.minutos, self.segundos))
        fechaNueva.minutos -= numeroMinutos

        while fechaNueva.minutos < 0:
            fechaNueva.hora -= 1
            fechaNueva.disminuirDiaHora()
            fechaNueva.disminuirAnoMesPorDias()
            fechaNueva.minutos += 60

        return fechaNueva

    def sumarSegundos(self, numeroSegundos):
        fechaNueva = Fecha((self.ano, self.mes, self.dia,
                            self.hora, self.minutos, self.segundos))
        fechaNueva.segundos += numeroSegundos
        numeroDiasMesActual = fechaNueva.__numeroDiasMes[fechaNueva.mes]

        while fechaNueva.segundos > 59:
            fechaNueva.segundos -= 60
            fechaNueva.minutos += 1
            fechaNueva.aumentarHoraMinutos()
            fechaNueva.aumentarDiaHora()
            fechaNueva.aumentarMesDia(numeroDiasMesActual)
            fechaNueva.aumentarAnoMes()
            numeroDiasMesActual = fechaNueva.__numeroDiasMes[fechaNueva.mes]

        return fechaNueva

    def restarSegundos(self, numeroSegundos):
        fechaNueva = Fecha((self.ano, self.mes, self.dia,
                            self.hora, self.minutos, self.segundos))
        fechaNueva.segundos -= numeroSegundos

        while fechaNueva.segundos < 0:
            fechaNueva.minutos -= 1
            fechaNueva.disminuirHoraMinutos()
            fechaNueva.disminuirDiaHora()
            fechaNueva.disminuirAnoMesPorDias()
            fechaNueva.segundos += 60

        return fechaNueva
