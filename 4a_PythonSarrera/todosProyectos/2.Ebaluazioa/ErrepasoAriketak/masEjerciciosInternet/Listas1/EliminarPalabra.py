"""
Listas (1) - 4
Escriba un programa que permita crear una lista de palabras y que,
a continuación, pida una palabra y elimine esa palabra de la lista.

"""


def buscarElementoListaYEliminar():
    listaPalabras = []
    cantidadPalabras = int(input("Cuántas palabras tiene la lista? "))

    if (cantidadPalabras < 1):
        print("¡Imposible! ")
    else:
        for i in range(cantidadPalabras):
            palabraUser = input("Cuál es la palabra " + str(i + 1) + "? ")
            listaPalabras.append(palabraUser)
        print("La lista creada es: " + str(listaPalabras))

    borrar = input("\nQué palabra quieres eliminar? ")

    for i in range(len(listaPalabras) - 1, - 1, - 1):
        if listaPalabras[i] == borrar:
            del listaPalabras[i]

    print("Lista final: " + str(listaPalabras))


if __name__=="__main__":
    buscarElementoListaYEliminar()