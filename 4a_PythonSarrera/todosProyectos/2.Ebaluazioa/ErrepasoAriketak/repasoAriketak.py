
#ejercicio1
#https://www.lawebdelprogramador.com/codigo/Python/3053-Calcular-los-multiplos-de-3-y-5.html
import random
from datetime import datetime, date


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
    print(stringAdrian.si)
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


#ejercicio 9
def fechaDecirEstacion():
    hilabeteGuztiak = (
        'Urtarrila', 'Otsaila', 'Martxoa', 'Apirila', 'Maiatza', 'Ekaina', 'Uztaila', 'Abuztua', 'Iraila', 'Urria',
        'Azaroa',
        'Abendua');

    actualFecha = date.today()  #fecha de hoy

    primaveraInicio = date(2020, 3, 20)
    primaveraFinal = date(2020, 6, 21)
    print(primaveraFinal)

    inicioVerano = date(2020, 6, 21)
    finalVerano = date(2020, 9, 23)

    inicioOtoño = date(2020, 9, 23)
    finalOtoño = date(2020, 12, 21)

    inicioInvierno = date(2020, 12, 21)
    finalInvierno = date(2021, 3, 20)

    stringMes = input("Sartu hilabete baten izena (urtarrila, otsaila...): ").capitalize()
    diaMes = int(input("Sartu hilabetearen egun bat: "))

    numeroMes = hilabeteGuztiak.index(stringMes)

    # p.e.: año = 2020 - ya que al usuario no se le pide el valor del año
    fechaUsuario = date(2020, numeroMes + 1, diaMes)
    print("Fecha del usuario: " + str(fechaUsuario))

    if (fechaUsuario > actualFecha):
        print("no")
    else:
        print("si")


#ejercicio 10
def tablaDeMultiplicar():
    zenbakia = int(input("Sartu zenbaki bat (1-10): "))

    for i in range (1, 11):
        print(str(zenbakia) + " x " + str(i) + " = " + str(zenbakia * i))





#ejercicio 11
def trianguloConNumeros():

    numeroFilas = 9
    for row in range(numeroFilas):
        for col in range(0, row + 1):
            print(row + 1, end=" ")
        print()


#ejercicio12
def adivinarNumeroOculto():

    #print(random.randint(0, 9))

    numeroSecreto = random.randint(0, 9)
    zenbakiaUser = 30

    while zenbakiaUser != numeroSecreto:
        zenbakiaUser = int(input("Sartu 1-9 ren artean dagoen zenbaki bat: "))

    print("Numero del Programa: " + str(numeroSecreto))
    print("Numero del Usuario: " + str(zenbakiaUser))


#ejercicio 13
def darLaVueltaString():
    hitzaUser = input("Sartu hitz bat: ")

    print(hitzaUser[::-1])


#ejercicio 14
def numerosConTodosLosDigitosImpares():
    num1 = 100
    num2 = 400

    fullImpar = False

    for i in range(num1, num2):
        for x in str(i):
            if int(x) % 2 != 0:
                fullImpar = True
            else:
                fullImpar = False
                break;
        if (fullImpar) == True:
            print(i)


#ejercicio 15
def mediaDe3Numeros():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    num3 = random.randint(0, 10)

    print("Numero 1: " + str(num1))
    print("Numero 2: " + str(num2))
    print("Numero 3: " + str(num3))

    sumaTodos = num1 + num2 + num3;
    mediaNumeros = sumaTodos / 3;

    print("La media es: " + str(mediaNumeros))


#ejercicio 16
def sumaTodosLosElementosLista():
    listaNumeros = [3, 4, 2, 11];
    print(listaNumeros)
    sumaTodo = 0

    for i in (listaNumeros):
        sumaTodo += i
    print("La suma total es: " + str(sumaTodo))


#ejercicio 17
def multiplicarElementosLista():
    zenbakienZerrenda = [2, 2, 3, 4]
    print(zenbakienZerrenda)
    multiplicarTodo = 1
    #multiplicarTodo = zenbakienZerrenda[0]

    for i in (zenbakienZerrenda):
        multiplicarTodo = multiplicarTodo * i
    print("El resultado es: " + str(multiplicarTodo))


#ejercicio 18
def mayorElementoLista():

    listaDeNumeros = [2, 4, 56, 55]
    print(listaDeNumeros)

    handiena = max(listaDeNumeros)
    print("El mayor numero de la lista es: " + str(handiena))


#ejercicio 19
def menorElementoLista():
    listaDeNumeros = [2, 4, 56, 55]
    print(listaDeNumeros)

    txikiena = min(listaDeNumeros)
    print("El menor numero de la lista es: " + str(txikiena))


#prueba recorrer dígitos de un número
def recorrerNumero():
    numeroPrueba = 511
    fullImpar = False
    for x in str(numeroPrueba):
        if int(x) % 2 != 0:
            fullImpar = True
        else:
            fullImpar = False
            break;

    if fullImpar == True:
        print("El numero es full impar")
    else:
        print("No es del todo impar ")


#############################################
#recorrerNumero()   #prueba - recorrer digitos de un numero / caracteres de un string
fechaDecirEstacion()    #prueba - hacer pruebas con fechas

#multiplos5y7() #ejercicio 1
#cambioCelsiusFahrenheit() #ejercicio 2
#dibujarFigura()    #ejercicio 3
#paresEImparesDeUnaLista()   #ejercicio 4
#cambiarIteracionesCondiones() #ejercicio 5
#contarLetrasNumerosDeString() #ejercicio 6
#patronDibujarLetraA()   #ejercicio 7
#letraVocalOConsonante() #ejercicio 8

#mesDiaPerteneceAEstacion() #ejercicio 9 - Galdetu

#tablaDeMultiplicar()   #ejercicio 10
#trianguloConNumeros()  #ejercicio 11
#adivinarNumeroOculto() #ejercicio 12
#darLaVueltaString()    #ejercicio 13
#numerosConTodosLosDigitosImpares()  #ejercicio 14 - Galdetu
#mediaDe3Numeros()   #ejercicio 15
#sumaTodosLosElementosLista()    #ejercicio 16
#multiplicarElementosLista()     #ejercicio 17
#mayorElementoLista()   #ejercicio 18
#menorElementoLista()   #ejercicio 19

#https://python-para-impacientes.blogspot.com/2014/02/operaciones-con-fechas-y-horas.html