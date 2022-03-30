# Ejercicio 1- Luciano Bravo

nombredealumno= input (" Nombre del alumno ")
listadematerias=[]
listadematerias.append("ingles")
listadematerias.append("computacion")
listadematerias.append("matematica")
listadematerias.append("Biologia")
print (listadematerias, len(listadematerias))

ni1=float(input("inserte nota primer parcial de ingles "))
ni2=float(input("inserte nota segundo parcial de ingles "))
ni3=float(input("inserte nota tercer parcial de ingles "))

nc1=float(input("inserte nota primer parcial computacion "))
nc2=float(input("inserte nota segundo parcial computacion "))
nc3=float(input("inserte nota tercer parcial computacion "))

nm1=float(input("inserte nota primer parcial matematica "))
nm2=float(input("inserte nota segundo parcial matematica "))
nm3=float(input("inserte not tercer parcial matematica "))

bn1=float(input("inserte nota primer parcial biologia "))
bn2=float(input("inserte nota segundo parcial biologia "))
bn3=float(input("inserte nota tercer parcial biologia "))


ingles= (ni1+ni2+ni3)/3
computacion= (nc1+nc2+nc3)/3
matematica=(nm1+nm2+nm3)/3
Biologia=(bn1+bn2+bn3)/3

if ingles >= 8: 
    print (str(nombredealumno) + " ingles esta promocionado "+ " promedio fue = "+str(ingles))
elif ingles < 8 and ingles >= 6:
    print (str(nombredealumno) + " ingles esta aprobado "+ " promedio fue = "+str(ingles))
    
else: 
    print (str(nombredealumno) + " ingles esta desaprobado "+ " promedio fue = "+str(ingles))
    
if computacion >= 8: 
    print (str(nombredealumno) + " computacion esta promocionado "+ " promedio fue = "+str(computacion))
    
elif computacion < 8 and computacion >= 6:
    print (str(nombredealumno) + " computacion esta aprobado "+ " promedio fue = "+str(computacion))
    
else: 
    print (str(nombredealumno) + " computacion esta desaprobado "+ " promedio fue = "+str(computacion))
    

if matematica >= 8: 
    print (str(nombredealumno) + " matematica esta promocionado "+ " promedio fue = "+str(matematica))
    
elif matematica < 8 and matematica >= 6:
    print (str(nombredealumno) + " matematica esta aprobado "+ " promedio fue = "+str(matematica))
    
else: 
    print (str(nombredealumno) + " matematica esta desaprobado "+ " promedio fue = "+str(matematica))

if Biologia >= 8: 
    print (str(nombredealumno) + " Biologia esta promocionado "+ " promedio fue = "+str(Biologia))
    
elif Biologia < 8 and Biologia >= 6:
    print (str(nombredealumno) + " Biologia esta aprobado "+ " promedio fue = "+str(Biologia))
    
else: 
    print (str(nombredealumno) + " Biologia esta desaprobado "+ " promedio fue = "+str(Biologia))