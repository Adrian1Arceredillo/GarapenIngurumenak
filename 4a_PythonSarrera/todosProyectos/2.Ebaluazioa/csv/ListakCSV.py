
import csv

from csv import reader

with open('employee.txt', mode='r') as csv_file:
    csv_reader = reader(csv_file)#csv.DictReader(csv_file)
    listaCsv = list(csv_reader)

#imprimir nombre concreto
def izenaBilatu():
    with open('employee.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        izenaUser = input("Sartu langilearen izena: ").capitalize()
        for row in csv_reader:
            if line_count == 0:

                line_count += 1

            if row["Izena"] == izenaUser:
                print(f'\t{row["Izena"]}, {row["Abizeba"]}, {row["Soldata"]}\n ')

            line_count += 1


def nomberApellidoDelNum23():
    with open('employee.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        #input
        for row in csv_reader:
            if line_count == 0:

                line_count += 1
            if row["Adina"] == "23":
                print(f'\tBere datuak: {row["Izena"]}, {row["Abizeba"]}, {row["Adina"]}')

            line_count += 1


def verTodosLosLangiles():
    with open('employee.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'\nColumn names are {", ".join(row)}')
                line_count += 1
            print(
                f'\t{row["Zbki"]}, Bere adina: {row["Adina"]}, {row["Generoa"]}, {row["Soldata"]}, {row["Hileko_gastuak"]}, {row["Lanpostua"]}, {row["Kirola"]}, {row["Izena"]}, {row["Abizeba"]}, {row["Herria"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')


def sueldoSuperiorA():
    with open('employee.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        sueldoUser = input("Sartu soldata bat: ")
        for row in csv_reader:
            if line_count == 0:

                line_count += 1

            if row["Soldata"] > sueldoUser:
                print(f'\t{row["Izena"]}, {row["Abizeba"]}, {row["Soldata"]}\n ')

            line_count += 1


def pruebaSolMax():
    maxSoldata = "0"
    langilea = 0
    for i in range(1, len(listaCsv)):
        if listaCsv[i][3] > maxSoldata:
            maxSoldata = listaCsv[i][3]
            langilea = i
            #print(soldMax, f'\t{row["Izena"]}, {row["Abizeba"]} ')
    print(listaCsv[langilea][7] + " " + listaCsv[langilea][8] + " " + listaCsv[langilea][3])  #[langilea] = fila; [7] = columna deseada


def pruebaSolMin():
    minSoldata = listaCsv[1][3]
    langilea = 0
    for i in range(1, len(listaCsv)):
        if listaCsv[i][3] < minSoldata:
            minSoldata = listaCsv[i][3]
            langilea = i
            #print(soldMax, f'\t{row["Izena"]}, {row["Abizeba"]} ')
    print(listaCsv[langilea][7] + " " + listaCsv[langilea][8] + " " + listaCsv[langilea][3])



def ordenarPorEdades(): #ordenar por edades de MENOR a MAYOR
    masJoven = listaCsv[1][1]
    masViejo = listaCsv[1][1]
    edades = list()
    for i in range(1, len(listaCsv)):
        edades.append(listaCsv[i][1])
    print('Ordenatu gabe: ' + str(edades))

    #utilizando el metodo burbuja - #https://cdklhph.wordpress.com/2015/08/08/ordenamiento-burbuja/
    for i in range(1, len(edades)):
        for j in range(0, len(edades) - i):
            if (edades[j + 1] < edades[j]):
                aux = edades[j];
                edades[j] = edades[j + 1];
                edades[j + 1] = aux;
    print('Ordenatuta: ' + str(edades))
    #https://sites.google.com/site/fernandoagomezf/programacion-en-c/tips-de-programador-c/algoritmos/ordenacion-de-arrays-metodo-de-la-burbuja



def kirolikEz():
    with open('employee.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        #input
        for row in csv_reader:
            if line_count == 0:

                line_count += 1
            if row["Kirola"] == "Inoiz ez":
                print(f'\tBere datuak: {row["Izena"]}, {row["Abizeba"]}, {row["Adina"]}')

            line_count += 1



aukera = "afwff"
salir = False

while(aukera != 'i'):
    print('MENUA')
    print('-----------')
    print('a) Ikusi langile guztiak. ')
    print('b) Adierazi 23 urte dituen langilearen izena eta abizena.')
    print('c) Langile bat bilatu (sartu izena): ' )
    print('d) Soldata bat baino handiagoak direnak (sartu soldata bat)')
    print('e) Soldata HANDIENA bistaratu (+ izena))')
    print('f) Soldata TXIKIENA bistaratu (+ izena))')
    print('g) Kirola egiten ez dutenen lanpostua eta herria ')
    print('h) Txikienetik zaharrenera ordenatu ')
    print('i) Irten')

    print()

    aukera = input('Elige una opción: ')


    if (aukera == 'a'):
        print()
        verTodosLosLangiles()
        print('---------------------------------------------------------')
        print()

    elif (aukera == 'b'):
         nomberApellidoDelNum23()
         print('---------------------------------------------------------')
         print()

    elif (aukera == 'c'):
         izenaBilatu()
         print('---------------------------------------------------------')
         print()

    elif (aukera == 'd'):
         sueldoSuperiorA()
         print('---------------------------------------------------------')
         print()

    elif (aukera == 'e'):
         pruebaSolMax()
         print('---------------------------------------------------------')
         print()

    elif (aukera == 'f'):
         pruebaSolMin()
         print('---------------------------------------------------------')
         print()

    elif (aukera == 'g'):
         kirolikEz()
         print('---------------------------------------------------------')
         print()

    elif (aukera == 'h'):
         ordenarPorEdades()
         print('---------------------------------------------------------')
         print()

    elif (aukera == 'i'):
        print()
        print("Saliendo...\nFIN. ")
        break

    else:
        print('No se ha encontrado la opcion. ')
        print()



#https://realpython.com/python-csv/