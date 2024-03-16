""" Metodo de Transporte"""

#Inicializamos variables 
origenes = []
destinos = []

#Función que calcula el método de transporte
def MetodoTransporte() -> None:
    origenes.clear()
    destinos.clear()
    # obtenemos la cantidad de destinos y origenes
    cantidad_origenes = int(input('>>> Ingrese el número de orígenes: '))
    for i in range(cantidad_origenes):
        origenes.append(input(f'Ingrese el nombre del origen {i+1}: '))

    cantidad_destinos = int(input('>>> Ingrese el número de destinos: '))
    for i in range(cantidad_destinos):
        destinos.append(input(f'Ingrese el nombre del destino {i+1}: '))
        
    # Inicializamos las variables
    matriz_costos = []
    ofertas = []
    demandas = []

    for k in range(cantidad_origenes):
        datos = []

        for j in range(cantidad_destinos):
            datos.append(float(input(f'Costo unitario de {origenes[k]} hacia {destinos[j]}: ')))

        # Después de cargar la lista de datos la anexamos a la matriz de datos
        matriz_costos.append(datos)

        # Pedimos la oferta de la fila
        ofertas.append(float(input(f'Oferta de {origenes[k]}:')))

    for k in range(cantidad_destinos):
        demandas.append(float(input(f'Ingrese la demanda [{k+1}]:')))
    
    """ Mostramos la matriz """
    print('\nMatriz de datos:')
    for k in range(len(matriz_costos[0])):
        print(f'\t{destinos[k]}', end='')
    print('\tOferta')
    for j, fila in enumerate(matriz_costos):
        for valor in fila:
            print(f'\t{valor}', end='\t')
        print(f'\t{ofertas[j]}')
    print('Demanda ', end='')
    for valores in demandas:
        print(f'{valores}', end='\t\t')
    print('')

    """ Aplicamos el metodo de la esquina noroeste para obtener los resultados"""
    res = []
    col_res = []
    fil_res = []

    # Recorremos la matriz por cada fila
    for fila, lista in enumerate(matriz_costos):
        for columna in range(len(lista)):
            # Verificamos si no es una fila o columna ya resuelta
            if(columna not in col_res and fila not in fil_res):
                # En caso de que la oferta sea mayor que la demanda
                if(ofertas[fila] > demandas[columna]):
                    resultado = {
                        'valor': demandas[columna],
                        'coordenada': [fila, columna]
                    }
                    # Se guarda la columna resuelta incluida en el diccionario
                    col_res.append(columna)
                    res.append(resultado)

                    # Se resta el valor de la oferta
                    ofertas[fila] -= demandas[columna]
                    demandas[columna] = 0 # se anula el valo
                
                elif(demandas[columna] > ofertas[fila]):
                    # En caso de que la demanda sea mayor que la oferta
                    resultado = {
                        'valor': ofertas[fila],
                        'coordenada': [fila, columna]
                    }
                    # Guardamos la fila como terminada y anexamos el resultado
                    fil_res.append(fila)
                    res.append(resultado)

                    # Restamos el valor de la demanda con el de la oferta y ponemos en 0 la oferta
                    demandas[columna] -= ofertas[fila]
                    ofertas[fila] = 0
                
                # Caso en el que la oferta y demanda son iguales
                else:
                    # Guardamos cualquier dato de oferta o demanda
                    resultado = {
                        'valor': ofertas[fila],
                        'coordenada': [fila, columna]
                    }
                    # Guardamos la fila y columna como terminada
                    fil_res.append(fila)
                    col_res.append(columna)

                    # Guardamos el resultado
                    res.append(resultado)

                    # Ponemos en 0 la oferta y demanda
                    ofertas[fila] = 0
                    demandas[columna] = 0
    resultados = res

    """ Mostramos los resultados """
    print('\nResultados:')
    for k in range(len(demandas)):
        print(f'\t{destinos[k]}', end='')
    print('')
    for k in range(len(ofertas)):
        for j in range(len(demandas)):
            encontrado = False
            for resultado in resultados:
                if(resultado['coordenada'] == [k,j]):
                    print(f'\t{resultado["valor"]}', end='\t')
                    encontrado = True
            if not encontrado:
                print(f'\tNone', end='\t')
        print('')
    
    # Calculamos y mostramos los costos segun la lista de resultados
    print('\nCostos:')
    print('\tCantidad\tCosto\tCosto total')
    costo_total = 0

    for resultado in resultados:
        # Extraemos los valores importantes del diccionario
        valor = resultado['valor']
        coordenada = resultado['coordenada']
        costo = matriz_costos[coordenada[0]][coordenada[1]]
        costo_total += valor*costo
        
        print(f'\t{valor}\t\t{costo}\t{valor*costo}')

    print(f'\tTotal: {costo_total}\n')