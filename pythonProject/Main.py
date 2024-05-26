import time
import random

print("Wollen Sie den Resscourcenvektor selbst angeben oder aus einer Datei zugreifen? ")

while True:
    # Abfrage, ob man den Existing Rescource Vektor selbst eingibt oder durch eine Datei zugreift
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
        elif matrix == "Anforderungsmatrix":
            wahl1 = int(input(
                'Wollen Sie die Anforderungsmatrix selbst eingeben "1" oder eine zufällige Matrix generieren lassen "2"? '))
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
            elif matrix == "Anforderungsmatrix":
                print(f"\nDie Anforderungsmatrix ist: \n{matrix1[0]}\n{matrix1[1]}\n{matrix1[2]}\n")
            return matrix1
        elif wahl1 == 2:
            if matrix == "Belegungsmatrix":
                matrix = [[1, 0, 1],
                          [0, 1, 0],
                          [0, 0, 2]]
                print(f"\nDie Belegungsmatrix ist: \n{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n")
                return matrix

            elif matrix == "Anforderungsmatrix":
                rows = 3
                cols = 3
                max_values_per_row = [eResource[0], eResource[1], eResource[2]]  # Maximalwerte pro Zeile
                matrix = [[random.randint(0, max_values_per_row[row]) for _ in range(cols)] for row in range(rows)]
                # Ausgabe der Anforderungsmatrix
                print(f"\nDie Anforderungsmatrix ist: \n{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n")
                return matrix
        else:
            print("Die Eingabe war falsch! Bitte Option '1' oder '2' wählen!\n")


# Erstellung der Belegungsmatrix
alloc = matrix_erstellung("Belegungsmatrix")


def ressourcen_belegung(prozess, matrix):
    beListe = matrix[prozess - 1]
    if len(klasse1) >= beListe[0]:  # Prüft, ob es überhaupt noch verfügbare Ressourcen gibt
        for i in range(beListe[0]):
            r = klasse1.pop(0)  # zeigt und entfernt die erste ressource
            belegt1[0][prozess - 1].append(r)  # Macht die belegten Ressourcen zur Übersicht in eine Liste
            # print(f"Prozess {prozess} belegt Ressource der Klasse 1 ")
    else:
        print(f"Prozess {prozess} kann die Ressource der Klasse 1 nicht belegen!")  # Ressource ist nicht verfügbar

    if len(klasse2) >= beListe[1]:
        for i in range(beListe[1]):
            r = klasse2.pop(0)  # zeigt und entfernt die zweite ressource
            belegt1[1][prozess - 1].append(r)
            # print(f"Prozess {prozess} belegt Ressource der Klasse 2 ")
    else:
        print(f"Prozess {prozess} kann die Ressource der Klasse 2 nicht belegen!")

    if len(klasse3) >= beListe[2]:
        for i in range(beListe[2]):
            r = klasse3.pop(0)  # zeigt und entfernt die dritte ressource
            belegt1[2][prozess - 1].append(r)
            # print(f"Prozess {prozess} belegt Ressource der Klasse 3 ")
    else:
        print(f"Prozess {prozess} kann die Ressource der Klasse 3 nicht belegen!")


# Einfach nur fürs Design
print("Ressourcenrestvektor wird berechnet... ")

time.sleep(2)

# Überprüft, ob ein Prozess schon einmal komplett durchlaufen ist
wenn_ausgefuehrt = False
wenn_ausgefuehrt2 = False
wenn_ausgefuehrt3 = False


# Überprüfung, ob ein Deadlock vorhanden ist
def pruefe_deadlock(prozess):
    global wenn_ausgefuehrt
    global wenn_ausgefuehrt2
    global wenn_ausgefuehrt3

    beListe = req[prozess - 1]
    # Prüft, ein Prozess durchgeführt werden kann
    if len(klasse1) >= beListe[0] and len(klasse2) >= beListe[1] and len(klasse3) >= beListe[2]:
        if not wenn_ausgefuehrt and prozess == 1:
            return False
        if not wenn_ausgefuehrt2 and prozess == 2:
            return False
        if not wenn_ausgefuehrt3 and prozess == 3:
            return False
    else:
        return True


# Nachdem ein Programm durchlaufen ist, werden die Ressourcen freigegeben
def freigabe(prozess):
    for i in range(len(belegt1[0][prozess - 1])):
        re = belegt1[0][prozess - 1].pop(0)
        klasse1.append(re)
    for i in range(len(belegt1[1][prozess - 1])):
        re = belegt1[1][prozess - 1].pop(0)
        klasse2.append(re)
    for i in range(len(belegt1[2][prozess - 1])):
        re = belegt1[2][prozess - 1].pop(0)
        klasse3.append(re)
