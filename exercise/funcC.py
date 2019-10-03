#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" LISTA DE APROBADOS A PARTIR DE UN DICCIONARIO"""



def funcC(nombres):
    """
    Retorna una lista de los aprobados por Gauss ordenada de menor a mayor

    :param nombres: diccionario con nombres y calificaciones {'Juan': 100}
    :return: list. los nombres de los aprobados de menor a mayor calificación

    >>>funcC({'pedro':45, 'alberto':30, 'lucia': 55})
    ['pedro', 'lucia']
    """

    notas = list(nombres.values())
    promedio = sum(notas)/(len(notas))
    ordenado = [[nombres[i],i] for i in nombres if nombres[i]>=promedio]
    ordenado.sort()
    aprobados = [ordenado[i][1] for i in range(len(ordenado))]

    return aprobados

if __name__ == '__main__':
    nombres = {'pedro':45, 'alberto':30, 'lucia': 55}
    print(funcC(nombres))
