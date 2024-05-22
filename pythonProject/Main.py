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
#test
