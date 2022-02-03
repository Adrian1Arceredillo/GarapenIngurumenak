
#ejercicio1
#https://www.lawebdelprogramador.com/codigo/Python/3053-Calcular-los-multiplos-de-3-y-5.html


#ariketa 1
def multiplos5y7():
    zenbakia1 = 1500
    zenbakia2 = 2700

    for i in range(zenbakia1, zenbakia2):
        if (i % 5 == 0) & (i % 7 == 0):
            print(i)


#ariketa 2
def cambioCelsiusFahrenheit():  #c = (f - 32) * (5 / 9)     #f = (9/5 * c) + 32
    print("1- C to F ")
    print("2- F to C:")
    aukera = int(input("Zer egin nahi duzu) (1 edo 2) "))

    if aukera == 1:
        celsiusEntrada = int(input("Sartu C ren balio bat: "))
        f = (9/5 * celsiusEntrada) + 32
        print(f)
    elif aukera == 2:
        fahrenheitEntrada = int(input("Sartu F ren balio bat: "))
        c = (fahrenheitEntrada - 32) * (5 / 9)
        print(c)



#ariketa 3
numeroFilas = 5;
numeroCols = 5
def dibujarFigura():    #https://www.tutorialgateway.org/python-program-to-print-half-diamond-star-pattern/
    for row in range(numeroFilas):
        for col in range(0, row + 1):
            print("* ", end=" ")
        print()
    for row in range(1, numeroFilas):
        for col in range(row, numeroFilas):
            print("* ", end=" ")
        print()


#ariketa 4
def paresEImparesDeUnaLista():
    zerrenda = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bakoitiak = []
    bikoitiak = []

    for i in zerrenda:
        if (i % 2 == 0):
            bikoitiak.append(i)
        elif (i % 2 != 0):
            bakoitiak.append(i)

    print(bakoitiak)
    print(bikoitiak)


#ejercicio 5
def cambiarIteracionesCondiones():
    for i in range(1, 50):

        if (i % 3 == 0) & (i % 5 == 0):
            print("fizzbuzz")
        elif (i % 3 == 0):
            print("fizz")
        elif (i % 5 == 0):
            print("buzz")
        else:
            print(i)

#ejercicio 6
def contarLetrasNumerosDeString():
    letras = 0
    numeros = 0

    stringAdrian = "Python 3.2"
    for i in stringAdrian:
        if (i.isalpha()):
            letras += 1
        elif (i.isdigit()):
            numeros += 1

    print()
    print("String: " + stringAdrian)
    print("\tLetras: " + str(letras))
    print("\tNumeros: " + str(numeros))


#ejercicio 7
def patronDibujarLetraA():
    for i in range(0, 7):
        if i == 0:
            print(" *** ")
        elif (i == 3):
            print("*****")
        else:
            print("*   *")

#ejercicio 8
def letraVocalOConsonante():
    sarturikoLetra = input("Idatzi alfabetoko letra bat: ").lower()

    if (sarturikoLetra == 'a' or sarturikoLetra == 'e' or sarturikoLetra == 'i' or sarturikoLetra == 'o' or sarturikoLetra == 'u'):
        print("Sarturiko " + str(sarturikoLetra) + " letra BOCALA da. ")
    else:
        print("Sarturiko " + str(sarturikoLetra) + " letra KONTSONANTEA da. ")


#ejercicio 9
def mesDiaPerteneceAEstacion():
    hilabeteGuztiak = (
    'Urtarrila', 'Otsaila', 'Martxoa', 'Apirila', 'Maiatza', 'Ekaina', 'Uztaila', 'Abuztua', 'Iraila', 'Urria', 'Azaroa',
    'Abendua');

    # print(hilabeteGuztiak.indexof("Urtarrila"))

    stringMes = input("Sartu hilabete baten izena (urtarrila, otsaila...): ").capitalize()
    diaMes = int(input("Sartu hilabetearen egun bat: "))

    numeroMes = hilabeteGuztiak.index(stringMes)
    print(numeroMes + 1)
#############################################

#multiplos5y7() #ejercicio 1
#cambioCelsiusFahrenheit() #ejercicio 2
#dibujarFigura()    #ejercicio 3
#paresEImparesDeUnaLista()   #ejercicio 4
#cambiarIteracionesCondiones() #ejercicio 5
#contarLetrasNumerosDeString() #ejercicio 6
#patronDibujarLetraA()   #ejercicio 7
#letraVocalOConsonante() #ejercicio 8
mesDiaPerteneceAEstacion() #ejercicio 9



#https://python-para-impacientes.blogspot.com/2014/02/operaciones-con-fechas-y-horas.html