#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""funcB(lista), esta funcion suma los elementos dentro de una lista de numeros y retorna el tamaño de la lista 
seguido de la suma total de los mismos"""

lista= {4,5,6} #la variable lista, almacena los datos de la lista de numeros a sumar"""


"""definimos la funcion, y le enviamos los parametros necesarios funcB(variable_lista)"""

def funcB(lista):
	""" :inicializamos la variable que almacenara la suma de los elementos de nuestra lista
recorremos la lista utilizando el ciclo for para poder realizar la suma de sus elementos
	donde:
	   for variable_almacena_elemento in variable_lista
		--realizamos la operacion de la suma
	---asignamos a la variable_resultado el tamaño de la variable_lista,
		utilizando la funcion len() y el resultado de la suma.
	#len(variable_lista)- esta funcion nos permite obtener el tamaño y/o numero de elementos del objeto lista	
		retornamos la variable_resultado

	>>>funcB(lista{4,5,6})
		(3,15)
"""
	suma = 0  
	for i in lista:
	    suma += i
  
	resultado = (len(lista),suma)
	return resultado  


 #inicializamos el programa, e invocamos a la funcion
if __name__ == '__main__': 
    print(funcB(lista))


