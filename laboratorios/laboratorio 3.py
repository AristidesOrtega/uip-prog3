lista_super=[]
lista=("arroz","leche","tuna","cereal","jugo")
opcion=1
while opcion!='4':
	print('1-agregar\n2-eliminar\n3-ver\n4-salir')
	opcion=input()
	if opcion=='1':
	   print (lista)
	   articulo=input()
	   lista_super.append(articulo)
	elif opcion=='2':
		elim=input()
		lista_super.remove(elim)
	elif opcion=='3':
		print(lista_super)
		e=input()
