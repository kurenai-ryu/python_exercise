#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# a=input("Introduzca a");
# b=input("Introduzca b");
# c=input("Introduzca c");
def funcA(a ,b, c):
   """ Realiza el promedio de los argumentos a, b, c y lo despliega en pantalla """
   return ((a+b+c)//3)
   
if __name__ == '__main__':

    a = 4
    b = 10
    c = 6
    nombre = funcA.__name__
    documentacion = funcA.__doc__
    print(nombre,":")
    print(documentacion)  
    print("Para nuestro la funcA tiene los siguientes argumentos",a ,b ,c , "y el promedio es", funcA(a,b,c))
   
