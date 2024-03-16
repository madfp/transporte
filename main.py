from Clases.transporte import MetodoTransporte
from Clases.hungaro import MetodoHungaro

'''
Parcial IV - Problema de Asignación 
Elaborado por: Giancarlos Hernaiz y Marco De Freitas
'''

#Menú principal de nuestra aplicación
def menu() -> None:
  while(True):
    print("=========== Menu ===========\n1.- Problema de Transporte\n2.- Problema de Asignación\n3.- Salir")
    while True:
      try: 
        opcion = int(input("=> Seleccione alguna opción: "))
        if opcion in range(1, 4):
            break
        else:
            print("\n>>> Valor fuera de las opciones...\n")
      except: 
          print("\n>>> Ingresar datos necesarios...\n")
        
    # Filtrar la opcion del usuario 
    if opcion == 1:
        print(MetodoTransporte())
    elif opcion == 2:
        print(MetodoHungaro())
    else:
        print("\n>>> Ha salido del sistema...")
        break

if __name__ == "__main__":
    menu()