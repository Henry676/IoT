#! /usr/bin/env python --> Poner la cabecera porque con estos caracteres le damos a entender al SO que esto se ejecutara en el entorno de python
# -*- coding: encoding -*- ----> Ingresamos tabla de caracteres utf-8
#python -c "print(2+2)" Esto es para poder hacer pruebas para metodos


# Modo interactivo: "Modo calculadora" con "python" o "python3"

# Es posible traer valores anteriores con guiones bajos _, no es recomedable para estructuras ciclicas
print("Hello world");print("Programando en una");print("Sola linea");print(abs(-10));print(round(5.5));print(round(5.4));hola="Esta es una larga cadena que tiene \nVarias lineas de texto,";print(hola)

#r es para especificar a python que no interprete, es una cadena cruda por lo tanto debe de traer todos los caracteres


#Slides: Extraccion de subcadenas de caracteres
#Sintaxis: variable[posicion inicial, cantidad de caracteres despues del caracter inicial contando el caracter inicial]


#----------------Repasar practica
"""
>>> mensaje[2:4]    [posicion, cuantos caracteres quiero incluir despues del caracter en posicion tomando en cuenta el primer caracter]
'la'
>>> mensaje[0:4]
'Hola'
>>> mensaje
'Hola mundo'
>>> mensaje[5:10] [posicion 5 'm',H,o,l,a, ,m,u,n,d,o] --> Aqui solo se imprime mundo ya que 
'mundo'
>>> 


'Hola mund'
>>> mensaje[-6:9]
' mund'
>>> mensaje[-5:10]
'mundo'
>>> mensaje[-5:]
'mundo'
>>> mensaje[-5:-1]
'mund'

"""
