#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def funcC(nombres):
    notas = list(nombres.values())
    promedio = 0
    ordenado = []

    for i in notas:
        promedio += i
    promedio = promedio/(len(notas))

    for i in nombres:
        if nombres[i]>= promedio:
            ordenado.append([nombres[i],i])

    ordenado.sort()
    ordenado.reverse()

    aprobados = [ordenado[i][1] for i in range(len(ordenado))]

    return aprobados


if __name__ == '__main__':
    nombres = {'Diego': 98, 'Gustavo': 49, 'Limber': 100, 'Angela':99}
    aprobados = funcC(nombres)
