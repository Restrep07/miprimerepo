

def multiplicarTabla(x):

      
     for i in range (0, 51):

          resultado = int (i) * int(x)
          print(i, "x",x,"=",resultado)
     

entrada = input("Ingrese numero")
print("Tabla del numero : ",entrada)
multiplicarTabla(entrada)