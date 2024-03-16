from .helpers.Operaciones import esqNoroeste
from .helpers.Imprimir import mostrar_matriz_resultante, mostrar_matriz
from .helpers.Validar import lectura
from .helpers.Validar import REG_NUMBER, REG_FLOAT

def MetodoTransporte() -> None:
    # obtenemos la cantidad de destinos y origenes
    print('Ingrese la cantidad de destinos:')
    cantidad_destinos = int(lectura(REG_NUMBER))
    print('Ingrese la cantidad de origenes:')
    cantidad_origenes = int(lectura(REG_NUMBER))

    # Inicializamos las variables
    matriz_datos = []
    ofertas = []
    demandas = []

    for k in range(cantidad_origenes):
        datos = []

        for j in range(cantidad_destinos):
            print(f'Costo unitario del origen [{k+1}] hacia el destino [{j+1}]:')
            datos.append(float(lectura(REG_FLOAT)))

        # Después de cargar la lista de datos la anexamos a la matriz de datos
        matriz_datos.append(datos)

        # Pedimos la oferta de la fila
        print(f'Oferta del origen [{k+1}]:')
        ofertas.append(float(lectura(REG_FLOAT)))

    for k in range(cantidad_destinos):
        print(f'Ingrese la demanda [{k+1}]:')
        demandas.append(float(lectura(REG_FLOAT)))
    
    # Mostramos la matriz creada por el usuario
    print('\nMatriz de datos:')
    mostrar_matriz(matriz=matriz_datos, ofertas=ofertas, demandas=demandas)

    # Obtenemos los resultados por el metodo de la esquina noroeste
    resultados = esqNoroeste(matriz=matriz_datos, ofertas=ofertas, demandas=demandas)

    # Mostramos los resultados
    print('\nResultados:')
    mostrar_matriz_resultante(resultados=resultados, ofertas=len(ofertas), demandas=len(demandas))
    
    # Calculamos y mostramos los costos segun la lista de resultados
    print('\nCostos:')
    print('\tCantidad\tCosto\tCosto total')
    costo_total = 0

    for resultado in resultados:
        # Extraemos los valores importantes del diccionario
        valor = resultado['valor']
        coordenada = resultado['coordenada']
        costo = matriz_datos[coordenada[0]][coordenada[1]]
        costo_total += valor*costo
        
        print(f'\t{valor}\t\t{costo}\t{valor*costo}')

    print(f'\tTotal: {costo_total}\n')