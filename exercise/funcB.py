#!/usr/bin/env python2
# -*- coding: utf-8 -*-
lista= {4,5,6}

def funcB(lista):
	cantidad = len(lista)
	suma = 0
	for i in lista:
	    suma += i
  
	resultado = (cantidad,suma)
	return resultado  

if __name__ == '__main__':
    print(funcB(lista))


