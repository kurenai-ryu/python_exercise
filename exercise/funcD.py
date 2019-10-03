#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def funcD(cadena):
   """Invertir cadenas o listas es posible utilizar el operador slice
   NombreDeCadena [inicio : fin : paso]
   
   Que permite extraer los elementos de NombreDeCadena
   * Cuando no se tiene inicio comienza en el primer elemento de NombreDeCadena
   
   * Cuando no se registra un fin, terminará en el último elemento de NombreDeCadena
   
   * El paso negativo, permite recorrer hacia atrás, por lo que inicio y fin se invierten
   
   >>>funcD("Hola Mundo")
   odnuM aloH
   """
   return cadena[::-1]

if __name__ == '__main__':

    print(cadena)
