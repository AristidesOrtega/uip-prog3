#Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:45:13) [MSC v.1600 64 bit (AMD64)] on win32
#Type "copyright", "credits" or "license()" for more information.
#>>> #Aristides Ortega
x =0
comprad=0
while x<5:
        cliente =input ("introduce el nombre del cliente: ")
        compra = int(input("introduce el valor de la compra: "))
        x+=1
        if compra >= 500:
                comprad= compra-(compra*0.30)
                print ("Su compra es de: {0} ".format(comprad))
        else:
                if compra >= 200:
                    comprad = compra -(compra *0.20)
                    print ("Su compra es de: {0} ".format(comprad))
                else:
                        if compra <= 200:
                                comprad = compra -(compra *0.10)
                                print ("Su compra es de: {0} ".format(comprad))
                                
else:  
          ("Su compra es de: {0} ".format(compra))
          
