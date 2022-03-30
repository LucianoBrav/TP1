# Ejercicio 10- Luciano Bravo





from gettext import install
import random
from random import randint, uniform,random


numeroaleatorio= randint(0,20)
for i in range (5):
    numerodeusuario= int (input("pasame un numero"))
    if numeroaleatorio == numerodeusuario:
        print ("advinaste el numero UWU")
        break
    else: 
        print ("no adivinaste el numero")