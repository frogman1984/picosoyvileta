import csv
import sys

resultados = []
with open('090720.csv', 'r') as theFile:
    reader = csv.DictReader(theFile)
    #print("Meter el codigo de barras de producto:\n")
    number = input("Meter el codigo de barras de producto:\n")
    # El codigo de barras de pelele gatos es: 1128002716
    for line in reader:
        # line is { 'workers': 'w0', 'constant': 7.334, 'age': -1.406, ... }
        # e.g. print( line[ 'workers' ] ) yields 'w0'
        #print(line['SKU'], line['Nombre'], line['Precio rebajado'], line['Precio normal'])
        if number in line['Superior']:
            resultados.append(line)
            #print(line['Nombre'], line['Inventario'], line['Precio rebajado'], line['Precio normal'], line['Valor(es) del atributo 1'])


for i in range(len(resultados)):
    print("los resultados son:")
    print(i, resultados[i])

