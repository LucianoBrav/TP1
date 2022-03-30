# Ejercicio 7- Luciano Bravo



nombre=(input(" inserte nombre "))
edad=float(input(" inserte edad "))
dinero=float(input(" inserte dinero "))
hambre=float(input(" inserte medida de hambre de 0 a 10 ")) 


if hambre >=7 or (dinero <100 and edad <18):
    print ("hola "+ str(nombre) + "vas a comer a lo de tus padres?")

elif edad >34 and dinero >500 and hambre >5:
    print ("hola "+ str(nombre) + " hay asado hoy? ")

elif edad <35:
    print ("hola "+ str(nombre) + "eres una persona joven ya que tu edad es" + str(edad))