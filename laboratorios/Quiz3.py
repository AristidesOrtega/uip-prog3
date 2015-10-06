#Dado un intervalo de tiempo en segundos, calcular los segundos
#restantes que corresponden para convertirse exactamente en minutos
#Este programa debe funcionar para 5 oportunidades
#Aristides Ortega
for n in range(0,5):
        seg = int(input("Introduce la cantidad de segundos "))
        minutos = seg/60
        if minutos != 0:
                segundos = 60-seg %60
                print("Le faltan {0}, segundos para llegar al minuto".format(segundos))
