import pandas

resultados = []
archivo = pandas.read_csv('090720.csv')
#number = input("Meter el codigo de barras de producto:\n")
number = "1128002716"
# El codigo de barras de pelele gatos es: 1128002716
print(number[2:-2])
producto = (archivo[archivo['SKU'].str.contains(number, na=False)])
# Para sacar el index del producto cuyo CCBB es el que queremos
nproducto = (producto.index.item())
print(nproducto)
# Para sacar el nombre del producto cuyo CCBB es el que queremos.
vnombre = archivo.iloc[nproducto]['Nombre']
print(vnombre)
# Para sacar todas las lineas cuyo nombre sea el del producto en cuestion
variaciones = (archivo[archivo['Nombre'].str.contains(vnombre, na=False)])
#print(variaciones)
# Para quitar la fila del producto madre
variaciones = variaciones.drop([nproducto])
# Para quedarnos solo con la parte de los precios
acambiar= variaciones[['Nombre', 'Precio normal', 'Precio rebajado']]
print(acambiar)
indices = (acambiar.index.tolist())
print(indices)
for i in indices:
    print(i)
    precio_rebajado = input("Precio rebajado para el "+str(i)+": ")
    fila = archivo.iloc[i]
    ### Para cambiar el precio rebajado a la linea i
    archivo.at[i, 'Precio rebajado'] = str(precio_rebajado)
    #archivo.loc[i, ['Publicado', 'Precio rebajado', 'Precio normal']]
    print('Precios Cambiados')


print(archivo.loc[94, ['Nombre','Publicado', 'Precio rebajado', 'Precio normal']])


# Para printar la linea 94 y con las columnas ahi marcadas
#print(archivo.loc[nproducto, ['Nombre','Publicado', 'Precio rebajado', 'Precio normal']])
# Para sustituir valores
# archivo.loc[94, ['Publicado', 'Precio rebajado', 'Precio normal']]