# Ejercicio 9- Luciano Bravo


import math

operacionmate = input("¿que operacion matematica queres realizar?")
primernumero = input("inserte primer numero")
segundonumero = input("inserte segundo numero")


def suma(num1, num2):
    return (int(num1) + int(num2))

def resta(num1, num2):
    return (int(num1) - int(num2))

def multiplicar(num1, num2):
    return (int(num1) * int(num2))

def dividir(num1, num2):
    return (float(num1) / float(num2))


if operacionmate == "suma" or operacionmate == "+":
    if str.isdigit(primernumero) and str.isdigit(segundonumero):
        print(suma(primernumero, segundonumero))
    else:
        print("Syntax error")
elif operacionmate == "resta" or operacionmate == "-":
    if str.isdigit(primernumero) and str.isdigit(segundonumero):
        print(resta(primernumero, segundonumero))
    else:
        print("Syntax error")
elif operacionmate == "multiplicar" or operacionmate == "":
    if str.isdigit(primernumero) and str.isdigit(segundonumero):
       print(multiplicar(primernumero, segundonumero))
    else:
        print("Syntax error")

else:
    if str.isdigit(primernumero) and str.isdigit(segundonumero):
        print(dividir(primernumero, segundonumero))
    else:
        print("Syntax error")
    
    