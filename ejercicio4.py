import random
#lista

def listaAleatorios(n):
      lista = [0]*n  
      for i in range(len(lista)):
          lista[i] = random.randint(1, n+1)
      print ("Esta es la lista aleatoria de numeros ",lista)
      return lista
      

def numNaturales (lista):
   resultado = 0
   arrPares = []
   arrNoPares = []
   for i in range(len(lista)):

       resultado = int(lista[i]%2)
      
       if(resultado == 0):
           arrPares.append(lista[i])
      
           
       else:
            arrNoPares.append(lista[i])
   print("Estos son los numeros pares del arreglo :", arrPares)
   print("Estos son los numeros no pares del arreglo :", arrNoPares)
      
numero = int (input("Ingrese el numero N de numeros a mostrar"))
numNaturales(listaAleatorios(numero))
