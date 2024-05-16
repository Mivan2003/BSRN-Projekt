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
