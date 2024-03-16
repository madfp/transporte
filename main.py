from Clases.transporte import seleccion_transporte 
from Clases.hungaro import seleccion_hungaro

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
        
    # Acceder al menu de la opcion 
    if opcion == 1: # Carga categoria
        print(seleccion_transporte())
    elif opcion == 2: # Agrega categoria
        print(seleccion_hungaro())
    else:
        print("\n>>> Ha salido del sistema...")
        break

# Correr la funcion principal
if __name__ == "__main__":
    menu()