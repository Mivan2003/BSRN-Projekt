import time
import random

print("Wollen Sie den Resscourcenvektor selbst angeben oder aus einer Datei zugreifen? ")

while True:
    # Abfrage ob man den Existing Rescource Vektor selbst eingibt oder durch eine Datei zugreift
    eingabe = input('Tippen Sie "d" ein für die Datein oder "s", wenn Sie es selbst eingeben wollen: ')
    if eingabe == "s":
        print("Eingabe ist s")
        # Erstellung des Ressourcenvektors durch eigene Eingabe
        print("Geben Sie nun die Ressourcen ein.")
        eResource = [int(input("Klasse 1: ")), int(input("Klasse 2: ")), int(input("Klasse 3: "))]
        print(f"Der Ressourcenvektor ist: {eResource}")
        break
    elif eingabe == "d":
        print("Eingabe ist d")
        # Erstellung des Ressourcenvektors mithilfe einer Datei
        datei = open(input("Geben Sie den Dateinamen ein: "), "r")
        print(f"Der Ressourcenvektor ist: {datei.read()}")
        break
    else:
        print("Eingabe war falsch")

# Erstellung der Klassen
klasse1 = []
klasse2 = []
klasse3 = []

# Eine liste mit belegten Ressourcen, um die später wieder freizugeben
belegt1 = [[], [], []], [[], [], []], [[], [], []]


# Erstellung der Ressourcen
def add_ressource(klasse):
    for i in range(eResource[klasse - 1]):
        name = "r." + str(i)
        # print("Ressource erstellt") Best채tigung der Erstellung
        if klasse == 1:
            # Wenn 1, dann wirds in Klasse 1 hinzugefügt usw.
            klasse1.append(name)
        elif klasse == 2:
            klasse2.append(name)
        elif klasse == 3:
            klasse3.append(name)
        else:
            print("Einfügen der Ressource in die Lise, fehlgeschlagen!")


# Erstellung der Ressourcenlisten
add_ressource(1)
add_ressource(2)
add_ressource(3)


def matrix_erstellung(matrix):
    wahl1 = None
    while True:
        if matrix == "Belegungsmatrix":
            wahl1 = int(input(
                'Wollen Sie die Belegungsmatrix selbst eingeben "1" oder die, im vorhinein festgelegte Matrix benutzten "2"? '))
        if wahl1 == 1:
            print("Die Matrix besteht aus 3 Prozessen und 3 Klassen. "
                  "Bitte geben Sie nun die Matrix an:")
            # allgemeine Belegungsliste
            matrix1 = [
                [int(input("Prozess 1, Klasse 1: ")), int(input("Prozess 1, Klasse 2: ")),
                 int(input("Prozess 1, Klasse 3: "))],
                [int(input("Prozess 2, Klasse 1: ")), int(input("Prozess 2, Klasse 2: ")),
                 int(input("Prozess 2, Klasse 3: "))],
                [int(input("Prozess 3, Klasse 1: ")), int(input("Prozess 3, Klasse 2: ")),
                 int(input("Prozess 3, Klasse 3: "))]]
            if matrix == "Belegungsmatrix":
                print(f"\nDie Belegungsmatrix ist: \n{matrix1[0]}\n{matrix1[1]}\n{matrix1[2]}\n")
        elif wahl1 == 2:
            if matrix == "Belegungsmatrix":
                matrix = [[1, 0, 1],
                          [0, 1, 0],
                          [0, 0, 2]]
                print(f"\nDie Belegungsmatrix ist: \n{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n")
                return matrix


# Erstellung der Belegungsmatrix
alloc = matrix_erstellung("Belegungsmatrix")
