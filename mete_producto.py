import pandas
from funciones_meter_producto_web import *

resultados = []
archivo = pandas.read_csv('090720.csv')
nultimo = archivo.tail(1).index.start
print('Empezamos...')
print('El ID será: '+str(nultimo+1)+'\n')
tipo = input("Tipo:\n 1) Variable \n 2) Variation")
if tipo == "1":
    tipo = 'variable'
else:
    tipo = 'variation'
print(tipo)
nombre = input("Nombre de producto: ")
publicado = 1
destacado = 0
esvisible = 'visible'
descripcion = input('Meta la descripcion: \n')
inicio_rebajas = input('Fecha inicio rebajas:')
fin_rebajas = input('Fecha fin rebajas:')
estado_impuesto = "taxable"
if tipo == "1":
    clase_impuesto = "parent"
else:
    clase_impuesto = "21"
print(clase_impuesto)
eninventario = 1
esta_en_inventario = 1
permitir_reservas = 0
vendido_individualmente = 0
permitir_valoraciones = 0
precio_rebajado = input("Cual será el precio REBAJADO? - \n")
precio_normal = input("Cual será el precio NORMAL? - \n")
numero = input("""Cual seria la categoria? 
                         1 - Bañadores
                         2 - Camisas / Polos
                         3 - Camisetas
                         4 - Chaquetas
                         5 - Complementos
                         6 - Conjuntos
                         7 - Interiores
                         8 - Pantalones
                         9 - Pijamas
                         10 - Vestidos / Faldas \n""")

nombre_categoria = categoria_producto(numero)
print(nombre_categoria)