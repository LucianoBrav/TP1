# Ejercicio 8- Luciano Bravo




nombreyapellido=input("inserte nombre y apellido ")
añodenacimiento=int(input("inserte año de nacimiento "))
contraseña=input("inserte contraseña ")

def contar_vocales(cadena):
    contador = 0
    for letra in cadena:
        if letra.lower() in "aeiou":
            contador += 1
    return contador

def contar_numeros_años(num):
    contador = 0
    
    contador += len(str(num))

    return contador


contar_vocales(nombreyapellido)
contar_numeros_años(añodenacimiento)

if contar_vocales(nombreyapellido) >= 3:
    if contar_numeros_años(añodenacimiento) < 5:
        if len(contraseña) >= 8 and len(contraseña) <= 16:
            print("hola " + nombreyapellido + " como estas? ")
        else:
            print("la contraseña ingresada no debe de tener menos de 8 caracteres y no debe superar los 16 caracteres y debe contener alguno de estos simbolos ! “ # $ % & . - ")
    else:
        print("el año de nacimiento no es correcto, no debe de contener mas de 4 digitos")
else:
    print("el nombre ingresado no es correcto, debe contener al menos 3 vocales")