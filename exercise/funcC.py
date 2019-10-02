#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def funcC(nombres):
    notas = list(nombres.values())
    promedio = 0
    aprobados = []
    for i in notas:
        promedio += i
    promedio = promedio/(len(notas))

    for i in nombres:
        if nombres[i]>= promedio:
            aprobados.append(str(i))

    print(aprobados)


if __name__ == '__main__':
    nombres = {'Diego': 100, 'Gustavo': 49, 'Limber': 100, 'Angela':100}
    funcC(nombres)
