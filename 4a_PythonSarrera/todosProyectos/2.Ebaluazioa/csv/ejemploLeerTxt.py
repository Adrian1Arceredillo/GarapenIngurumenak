"""
Leer un archivo txt y decir lo siguiente:
    - cuántas líneas/filas tiene
    - cuántos caracteres hay en cada línea/fila
    - contar cuántas veces aparece la letra 'A' (o 'a')
"""

import csv

from csv import reader

with open('ejemplo.txt', mode='r') as f:
    f = f.readlines()


"""def verNumeroFilas():
    line_count = 0
    for i in range(1, len(listaCsv)):
        if line_count == 0:
            print("\nLas columnas son: " + str(listaCsv[0]))
            line_count += 1

        line_count += 1
    print(f'\nHay un total de {line_count} líneas.')

"""

def contarCaracteresCadaLinea():

    stringCadaLinea = ""    #String que guardará el contenido de cada línea
    caracteresCadaLinea = 0
    for i in f:
        stringCadaLinea = i
        print(str(len(stringCadaLinea)))




#verNumeroFilas()
contarCaracteresCadaLinea()