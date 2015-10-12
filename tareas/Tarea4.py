#Dado un intervalo de tiempo en minutos, calcular los 
#días, horas y minutos correspondientes.
#Aristides Ortega
tiempo = int(input("Introduce la cantidad de minutos "))
dias = tiempo/1440
x = tiempo %1440
horas =x/60
minutos= x%60
print ("{0} dias, {1} minutos, {2} horas".format(dias,minutos,horas))
