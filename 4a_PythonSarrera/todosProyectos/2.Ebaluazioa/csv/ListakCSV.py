
import csv

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


#si queremos imprimir solamente una columna (p.e. el nombre de los trabajadores)





aukera = "afwff"
salir = False

while(aukera != 'e'):
    print('MENUA')
    print('-----------')
    print('a) Ikusi langile guztiak. ')
    print('b) Adierazi 23 urte dituen langilearen izena eta abizena.')
    print('c) Langile bat bilatu (sartu izena): ' )
    print('d) Soldata bat baino handiagoak direnak (sartu soldata bat)')
    print('e) Irten')

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
        print()
        print("Saliendo...\nFIN. ")
        break

    else:
        print('No se ha encontrado la opcion. ')
        print()



#https://realpython.com/python-csv/