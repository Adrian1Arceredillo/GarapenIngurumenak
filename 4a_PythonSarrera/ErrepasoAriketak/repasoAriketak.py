
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






#cambioCelsiusFahrenheit()
dibujarFigura()