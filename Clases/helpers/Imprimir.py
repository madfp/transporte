def mostrar_matriz(matriz:list[list[float]], ofertas=[], demandas=[]) -> None:    
    # Imprimimos el encabezado de la tabla
    for k in range(len(matriz[0])):
        print(f'\tDestino {k+1}', end='')
    print('\tOferta')

    # Imprimimos los valores de la tabla
    for j, fila in enumerate(matriz):
        for valor in fila:
            print(f'\t{valor}', end='\t')

        print(f'\t{ofertas[j]}')
    
    print('Demanda ', end='')
    for valores in demandas:
        print(f'{valores}', end='\t\t')

    print('')


def mostrar_matriz_resultante(resultados:list[dict], ofertas: int, demandas:int) -> None:

    for k in range(demandas):
        print(f'\tDestino {k+1}', end='')
    print('')
    
    for k in range(ofertas):
        for j in range(demandas):
            encontrado = False
            for resultado in resultados:
                if(resultado['coordenada'] == [k,j]):
                    print(f'\t{resultado['valor']}', end='\t')
                    encontrado = True
            
            if not encontrado:
                print(f'\tNone', end='\t')
        print('')


def mostrar_matriz_hungaro(resultados:list[list]) -> None:
    print('Matriz de resultados:')
    for k in range(len(resultados[0])):
        print(f'\tPuesto {k+1}', end='')
    print('')

    for k, fila in enumerate(resultados):
        print(f'Trab {k+1}', end='')
        for valor in fila:
            print(f'\t{valor}', end='\t')
        print('')