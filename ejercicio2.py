
import random


def listaAleatorios():
      lista = [0]*10  
      for i in range(len(lista)):
          lista[i] = random.randint(0, 10)
      print("Lista de numeros Aleatorios :",lista)
      return lista

def promedio (lista):
   resultado = 0
   for i in range(len(lista)):
      
       resultado += int(lista[i])

   resultado = resultado /len(lista)   
   return resultado  

print("promedio",promedio(listaAleatorios()))


