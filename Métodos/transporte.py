#! CÓDIGO DE TRANSPORTE DE ACRÓPOLIS - MÉTODO DE TRANSPORTE
# from pulp import *

# ### Ciudades
# origen = ['LA','Detroit','New Orleans']
# destino = ['Denver','Miami']

# oferta = {'LA': 1000, 'Detroit' : 1500, 'New Orleans': 1200}
# demanda = {'Denver': 2300, 'Miami' : 1400}

# costo_envio ={'LA':{'Denver': 80, 'Miami' : 215},
#              'Detroit':{'Denver': 100, 'Miami' : 108},
#              'New Orleans': {'Denver': 102, 'Miami' : 68}}

# ### Declaramos la función objetivo... nota que buscamos minimizar el costo(LpMinimize)
# prob = LpProblem('Transporte', LpMinimize)

# rutas = [(i,j) for i in origen for j in destino]
# cantidad = LpVariable.dicts('Cantidad de Envio',(origen,destino),0)
# prob += lpSum(cantidad[i][j]*costo_envio[i][j] for (i,j) in rutas)
# for j in destino:
#     prob += lpSum(cantidad[i][j] for i in origen) == demanda[j]
# for i in origen:
#     prob += lpSum(cantidad[i][j] for j in destino) <= oferta[i]
# ### Resolvemos e imprimimos el Status, si es Optimo, el problema tiene solución.
# prob.solve()
# print("Status:", LpStatus[prob.status])

# ### Imprimimos la solución
# for v in prob.variables():
#     if v.varValue > 0:
#         print(v.name, "=", v.varValue)
# print('El costo mínimo es:', value(prob.objective))

origenes = []
destinos = []
matriz_costos = []

oferta = {}
demanda = {}
def seleccion_transporte(): 
    
    nro_origenes = int(input('>>> Ingrese el número de orígenes: '))
    for i in range(nro_origenes):
        origenes.append(input(f'Ingrese el nombre del origen {i+1}:'))
        oferta[origenes[i]] = int(input(f'Oferta del destino {origenes[i]}: '))
        
    nro_destinos = int(input('>>> Ingrese el número de destinos: '))
    for i in range(nro_destinos):
        destinos.append(input(f'Ingrese el nombre del destino {i+1}:'))
        demanda[destinos[i]] = int(input(f'Demanda del destino {destinos[i]}: '))

    return(origenes, destinos, oferta, demanda)