
import random


def listaAleatorios(n):
      lista = [0]*n  
      for i in range(len(lista)):
          lista[i] = random.randint(1, n+1)
      print ("Esta es la lista aleatoria de numeros naturales",lista)
      return lista
      

def numNaturales (lista):

   for i in range(len(lista)):
      
        print("Estos son los numeros naturales :", int(lista[i]))
      
numero = int (input("Ingrese el numero N de numeros naturales a mostrar"))
numNaturales(listaAleatorios(numero))