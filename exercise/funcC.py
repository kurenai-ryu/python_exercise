#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def funcC(nombres):
    notas = list(nombres.values())
    promedio = sum(notas)/(len(notas))
    ordenado = [[nombres[i],i] for i in nombres if nombres[i]>=promedio]
    ordenado.sort()
    aprobados = [ordenado[i][1] for i in range(len(ordenado))]

    return aprobados

if __name__ == '__main__':
    nombres = {'Diego': 98, 'Gustavo': 49, 'Limber': 100, 'Angela':99}
    print(funcC(nombres))
