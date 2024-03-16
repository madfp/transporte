from numpy import array, transpose, copy

""" Metodo principal - Metodo hungaro """
def MetodoHungaro():
    # inicializamos las variables
    cantidad_tareas= int(input('Ingrese la cantidad de Tareas: '))
    cantidad_trabajadores = int(input('Ingrese la cantidad de Trabajadores: '))

    matriz_datos = []

    # Procedemos a la carga inicial de datos
    for k in range(cantidad_trabajadores):
        # En cada iteración creamos una lista de valores
        datos = []

        for j in range(cantidad_tareas):
            datos.append(float(input(f'Costo unitario de la tarea [{k+1}] del trabajador [{j+1}]:')))

        # Después de cargar la lista de datos la anexamos a la matriz de datos
        matriz_datos.append(datos)
    
    # Si la matriz no es cuadrada la completamos con ceros hasta que sea cuadrada
    if cantidad_tareas != cantidad_trabajadores:
        for _ in range(abs(cantidad_tareas-cantidad_trabajadores)):
            matriz_datos.append([0 for _ in range(cantidad_tareas)])
    
    # Creamos la copia que sera la matriz de costos
    matriz_costos = [fila for fila in matriz_datos]

    # Usamos el algotimo del metodo hungaro para encontrar la matriz resultante
    matriz_resultado = metodo_hungaro(matriz=matriz_datos)

    """ Mostrar la matriz resultante """
    print('>>> Matriz de resultados:')
    for k in range(len(matriz_resultado[0])):
      print(f'\tPuesto {k+1}', end='')
    print('')
    for k, fila in enumerate(matriz_resultado):
      print(f'Trab {k+1}', end='')
      for valor in fila:
          print(f'\t{valor}', end='\t')
      print('')

    # Calculamos los costos
    print('\nCostos:')
    costos_hungaro(matriz_resultado, matriz_costos)

""" Funciones auxiliares """
# Funcion que resta el minimo de cada fila
def restar_minimo_fila(matriz:array) -> None:
    # Buscamos el numero mas pequeño por fila y lo restamos al resto de valores
    for k, fila in enumerate(matriz):
        menor = min(fila)
        # Si el menor es 0 no hacemos nada, caso contrario remplazamos la fila por una nueva con la diferencia de valores
        if (menor != 0): matriz[k] = [valor - menor for valor in fila]

# Funcion que elimina las filas que contienen mas ceros que lo pedido
def eliminar_filas(matriz:array, coordenadas_eliminadas:list[list], intersecciones:list[list], invertir=False, cant_ceros=1) -> int:
    # Definimos una funcion que retorna la cantidad de ceros de una lista
    cal_ceros = lambda lista: sum(valor == 0 for valor in lista)

    # Definimos una variable que sea la cantidad de eliminaciones
    cant_eliminaciones = 0

    for k, filas in enumerate(matriz):
        # Si la contiene mas ceros que lo pedido iniciamos a borrar filas
        cant_ceros_interes = 0

        # Buscamos si hay ceros que no han sido eliminados
        for j, valor in enumerate(filas):
            coordenadas = [k, j] if not invertir else [j, k]
            if coordenadas not in coordenadas_eliminadas and valor == 0:
                cant_ceros_interes += 1

        # Si la cantidad de ceros que no han sido eliminados es mayor que el requisito los eliminamos
        if cant_ceros_interes > cant_ceros:
            for j in range(len(filas)):
                coordenadas = [k, j] if not invertir else [j, k]
                # Si la coordenada creada en la iteracion existe en las eliminadas es una interseccion
                if coordenadas in coordenadas_eliminadas:
                    intersecciones.append(coordenadas)
                else:
                    coordenadas_eliminadas.append(coordenadas)
            # Agregamos las eliminaciones
            cant_eliminaciones += 1
    
    return cant_eliminaciones

# Funcion que retorna el menor valor de la matriz
def minimo_valor(matriz:array, coordenadas_eliminadas:list[list]) -> float:
    # Definimos el mayor valor posible
    menor = 999999999

    for k, filas in enumerate(matriz):
        for j, valor in enumerate(filas):
            coordenadas = [k, j]
            # Si la coordenada actual no fue eliminada y el menor guardado es mayor que el valor lo remplazamos
            if coordenadas not in coordenadas_eliminadas and menor > valor: menor = valor
    return menor

# Funcion que actualiza los valores de la matriz
def actualizar_valores(valor:float, matriz:array, coordenadas_eliminadas:list[list], intersecciones=list[list]):
    for k, fila in enumerate(matriz):
        new_fila = []
        for j, valor_columna in enumerate(fila):
            coordenadas = [k, j]
            # Si las coordenadas estan en las intersecciones sumamos el valor
            if  coordenadas in intersecciones:
                new_fila.append(valor_columna + valor)
            
            # Si la coordenada no fue eliminada lo restamos
            elif coordenadas not in coordenadas_eliminadas:
                new_fila.append(valor_columna - valor)
            
            # Si la coordenada fue eliminada lo guardamos normal
            else:
                new_fila.append(valor_columna)
        
        matriz[k] = new_fila

# Funcion que retorna la matriz resultante
def metodo_hungaro(matriz:list[list]) -> array:
    # Restamos los valores minimos a cada fila
    matriz = array(matriz)
    restar_minimo_fila(matriz=matriz)
    
    # Trasponemos la matriz y aplicamos el mismo algoritmo
    matriz = transpose(matriz)
    restar_minimo_fila(matriz=matriz)

    # Trasponemos la matriz para volver a la original
    matriz = transpose(matriz)

    # Definimos esta variable de control de ciclo
    cant_eliminaciones = 0

    while cant_eliminaciones < len(matriz[0]):
        coordenadas_eliminadas = []
        coordenadas_intersecciones = []

        # Vamos eliminando las filas por iteraciones
        cant_eliminaciones = eliminar_filas(
            matriz=matriz,
            coordenadas_eliminadas=coordenadas_eliminadas,
            intersecciones=coordenadas_intersecciones,
            invertir=False,
            cant_ceros=1
        )
        
        # Trasponemos la matriz y aplicamos lo mismo solo que cambiando el orden
        matriz = transpose(matriz)
        cant_eliminaciones += eliminar_filas(
            matriz=matriz,
            coordenadas_eliminadas=coordenadas_eliminadas,
            intersecciones=coordenadas_intersecciones,
            invertir=True,
            cant_ceros=0
        )

        # Si la cantidad de eliminaciones es mayor la longitud de la matriz paramos
        if cant_eliminaciones >= len(matriz[0]):
            matriz = transpose(matriz)
            break
        
        # Devolvemos la matriz a su estado original
        matriz = transpose(matriz)

        menor_valor = minimo_valor(matriz=matriz, coordenadas_eliminadas=coordenadas_eliminadas)

        actualizar_valores(
            valor=menor_valor,
            matriz=matriz,
            coordenadas_eliminadas=coordenadas_eliminadas,
            intersecciones=coordenadas_intersecciones
        )

    # Retornamos la matriz resultante
    return matriz

# Funcion que calcula los costos
def costos_hungaro(matriz_resultado, matriz_costo):
    # Creamos los indices de los trabajadores
    trabajadores = []
    for k in range(len(matriz_resultado)):
        trabajadores.append(f"Trab {k+1}")
    coordenadas_esperadas = [[k, k] for k in range(len(matriz_resultado))]
    while True:
        for k, fila in enumerate(matriz_resultado):
            cambiado = False
            for j, valor in enumerate(fila):
                if valor == 0 and  not cambiado:
                    # Intercambiamos las filas de la matriz
                    fila_aux = copy(matriz_resultado[k])
                    matriz_resultado[k] = matriz_resultado[j]
                    matriz_resultado[j] = fila_aux

                    # Intercambiamos los indices de los trabajadores
                    trabajador_aux = trabajadores[k]
                    trabajadores[k] = trabajadores[j]
                    trabajadores[j] = trabajador_aux

                    # Intercambiamos la matriz costo
                    fila_aux = matriz_costo[k]
                    matriz_costo[k] = matriz_costo[j]
                    matriz_costo[j] = fila_aux

                    # Marcamos que ya cambiamos las filas
                    cambiado = True
        
        encontradas = 0

        for coordenada in coordenadas_esperadas:
            if matriz_resultado[coordenada[0]][coordenada[1]] == 0:
                encontradas += 1
        
        if encontradas == len(matriz_resultado):
            break
    
    total = 0
    for k, trabajador in enumerate(trabajadores):
        total += matriz_costo[k][k]
        print(f'{trabajador}: {matriz_costo[k][k]}')
    print(f'Total: {total}')
    print('')