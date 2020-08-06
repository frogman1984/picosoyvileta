import pandas
from funciones_meter_producto_web import *

resultados = []
archivo = pandas.read_csv('060820.csv')
nultimo = archivo.tail(1).index.start
nid = archivo.iloc[nultimo]['ID']
print('Empezamos...')
print('El ID será: '+str(nid+1)+'\n')
tipo = input("Tipo:\n 1) Variable \n 2) Variation \n")
if tipo == "1":
    ntipo = 'variable'
else:
    ntipo = 'variation'
print(ntipo, tipo)
nombre = input("Nombre de producto: ")
sku = input("Codigo de barras: UNICO!! - ")
publicado = 1
destacado = 0
esvisible = 'visible'
descripcion = input('Meta la descripcion: ')
inicio_rebajas = input('Fecha inicio rebajas: ')
fin_rebajas = input('Fecha fin rebajas: ')
estado_impuesto = "taxable"
if tipo == "1":
    clase_impuesto = "parent"
else:
    clase_impuesto = "21"
print(clase_impuesto)
eninventario = 1
esta_en_inventario = 1
inventario = input("Cuantas unidades de este? - ")
permitir_reservas = 0
vendido_individualmente = 0
permitir_valoraciones = 0
precio_rebajado = input("Cual será el precio REBAJADO? - ")
precio_normal = input("Cual será el precio NORMAL? - ")
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
etiquetas = input("Mete las etiquetas separas por una coma: ")
if tipo == "2":
    superior = input("Meter el producto padre: ")
else:
    superior = ''
##############################
if tipo == "1":
    marca = get_marca()
    nombre_atributo1 = "Marca"
    valor_atributo1 = marca
    atributo_visible_1 = "1.0"
    atributo_global_1 = "1.0"
else:
    nombre_atributo1 = ""
    valor_atributo1 = ""
    atributo_visible_1 = ""
    atributo_global_1 = ""
if tipo == 1:
    posicion = "0.0"
else:
    posicion = input("Cual seria el orden de variacion?")
##################################
nino = input("""Es niño o niña?
        1 - Niña
        2 - Niño """)
if nino == "1":
    esnino = "Niña"
else:
    esnino = "Niño"
nombre_atributo2 = "niñ@"
valor_atributo2 = esnino
atributo_global_2 = "1"
atributo_visible_2 = "1"
######################################
talla = input("Introduzca la talla (Ejemplo:  18M, 24M) - ")
nombre_atributo3 = "Talla"
valor_atributo3 = talla
atributo_global_3 = "1"
atributo_visible_3 = "1"
########## EDAD ###############
edad = input("""Introduzca la edad: 
             Ejemplo(0-12 Meses, 18-24 Meses)""")

nombre_atributo4 = "Edad"
atributo_global_4 = "1"
atributo_visible_4 = "1"
valor_atributo4 = edad
#########################

### Proceso para meter en el CSV en una nueva fila

new_row = {
    'ID':nid+1,
    'Tipo':ntipo,
    'SKU':sku,
    'Nombre':nombre,
    'Publicado':publicado,
    '¿Está destacado?':destacado,
    'Visibilidad en el catálogo':esvisible,
    'Descripción':descripcion,
    'Estado del impuesto':estado_impuesto,
    'Clase de impuesto':clase_impuesto,
    '¿En inventario?':eninventario,
    'Inventario':inventario,
    '¿Permitir reservas de productos agotados?':0,
    '¿Vendido individualmente?':0,
    '¿Permitir valoraciones de clientes?':0,
    'Precio rebajado':precio_rebajado,
    'Precio normal':precio_normal,
    'Categorías':nombre_categoria,
    'Etiquetas':etiquetas,
    'Superior':superior,
    'Posición':posicion,
    'Nombre del atributo 1':nombre_atributo1,
    'Valor(es) del atributo 1':valor_atributo1,
    'Atributo visible 1':atributo_visible_1,
    'Atributo global 1':atributo_global_1,
    'Nombre del atributo 2':nombre_atributo2,
    'Valor(es) del atributo 2':valor_atributo2,
    'Atributo visible 2':atributo_visible_2,
    'Atributo global 2':atributo_global_2,
    'Nombre del atributo 3':nombre_atributo3,
    'Valor(es) del atributo 3':valor_atributo3,
    'Atributo visible 3':atributo_visible_3,
    'Atributo global 3':atributo_global_3,
    'Nombre del atributo 4':nombre_atributo4,
    'Valor(es) del atributo 4':valor_atributo4,
    'Atributo visible 4':atributo_visible_4,
    'Atributo global 4':atributo_global_4,
}
#append row to the dataframe
df_marks = archivo.append(new_row, ignore_index=True)

print('\n\nNew row added to DataFrame\n--------------------------')
print(df_marks)

df_marks.to_csv(r'salida.csv', index=False)
