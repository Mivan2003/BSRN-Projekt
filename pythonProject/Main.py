import time
import logging
import argparse

# Argument Parser für Kommandozeilen-Argumente
parser = argparse.ArgumentParser(description='Deadlock Simulator')
parser.add_argument('-l', '--logfile', type=str, default='simulator.log', help='Logdatei')
parser.add_argument('-mode', '--input_mode', type=str, choices=['s', 'd'], required=True,
                    help="Eingabemodus: 's' für selbst eingeben, 'd' für Datei")
parser.add_argument('-f', '--file', type=str, help='Datei zum Einlesen des Ressourcenvektors')
parser.add_argument('-bm', '--belegungsmatrix', type=str, help='Belegungsmatrixdatei')
parser.add_argument('-am', '--anforderungsmatrix', type=str, help='Anforderungsmatrixdatei')
args = parser.parse_args()

# Logging-Konfiguration für Logdatei-Dokumentation
logging.basicConfig(
    filename=args.logfile, level=logging.INFO)
logger = logging.getLogger('DeadlockSimulator')

# Die noch leere liste des Ressourcenvektors
eResource = []
# Damit man weiß ob Datei eingelesen werden soll oder ob man selbst schreiben will
eingabe = args.input_mode


# Abfrage am Anfang
def mode():
    global eResource
    global eingabe
    # Abfrage, ob man den Ressourcenvektor selbst eingibt oder durch eine Datei zugreift
    if args.input_mode == "s":
        # Erstellung des Ressourcenvektors durch eigene Eingabe
        print("\nGeben Sie nun die Ressourcen ein: ")
        eResource = [int(input("Klasse 1: ")), int(input("Klasse 2: ")), int(input("Klasse 3: "))]
        print(f"\nDer Ressourcenvektor ist: {eResource}\n")
        logger.info("Selbst Eingabe wird gewählt...")

    elif args.input_mode == "d":
        # Erstellung des Ressourcenvektors mithilfe einer Datei
        datei = args.file
        with open(datei, 'r') as file:
            # Lies die Zeilen der Datei und entferne Leerzeichen und Zeilenumbrüche
            lines = file.readlines()
            # Konvertiere die Zeichenketten in Ganzzahlen und füge sie der Liste hinzu
            eResource = [int(line.strip()) for line in lines]
        print(f"\nDer Ressourcenvektor ist: {eResource}\n")
        logger.info("Datei wird gewählt...")

    else:
        print("Eingabe war falsch")
        logger.info("Die Eingabe war falsch, der Benutzer soll es erneut versuchen...")


logger.info(f"Ressourcenvektor eingegeben: {eResource}\n")

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
        # print("Ressource erstellt") Bestätigung der Erstellung
        if klasse == 1:
            # Wenn 1, dann wirds in Klasse 1 hinzugefügt usw.
            klasse1.append(name)
        elif klasse == 2:
            klasse2.append(name)
        elif klasse == 3:
            klasse3.append(name)
        else:
            print("Einfügen der Ressource in die Lise, fehlgeschlagen!")
            logger.info("Bei der erstellung der Liste ist ein Fehler aufgetreten...")


# Nur zur überprüfung- wird später nicht benötigt
# rVektor = [klasse1, klasse2, klasse3]
# print(rVektor)

ausgefuehrt = False
ausgefuehrt2 = False


def matrix_erstellung(matrix):
    global ausgefuehrt
    global ausgefuehrt2

    while True:
        if args.belegungsmatrix and not ausgefuehrt:
            datei = args.belegungsmatrix
            with open(datei, 'r') as file:
                matrix = []
                for line in file:
                    # Entferne führende und abschließende Leerzeichen und teile die Zeile in einzelne Elemente
                    lst = line.strip().split()
                    # Konvertiere die Elemente in Integer (oder float, falls nötig)
                    lst = list(map(int, lst))
                    matrix.append(lst)
                logger.info("Belegungsmatrix Datei wird eingelesen...")
                print(f"\nDie Belegungsmatrix ist: \n{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n")
            ausgefuehrt = True
            return matrix
        elif args.anforderungsmatrix and not ausgefuehrt2:
            datei = args.anforderungsmatrix
            with open(datei, 'r') as file:
                matrix = []
                for line in file:
                    # Entferne führende und abschließende Leerzeichen und teile die Zeile in einzelne Elemente
                    lst = line.strip().split()
                    # Konvertiere die Elemente in Integer (oder float, falls nötig)
                    lst = list(map(int, lst))
                    matrix.append(lst)
                logger.info("Belegungsmatrix Datei wird eingelesen...")
                print(f"\nDie Anforderungsmatrix ist: \n{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n")
            ausgefuehrt2 = True
            return matrix
        else:
            print("Die Matrix besteht aus 3 Prozessen und 3 Klassen. "
                  "Bitte geben Sie nun die Matrix an:")
            logger.info("Matrix wird selbst erstellt werden...")
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


# Dadurch werden die Ressourcen der Belegungsmatrix blockiert
def ressourcen_belegung(prozess, matrix):
    logger.info(f"Die Ressourcen des {prozess}. Prozess werden belegt...")
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
    logger.info(f"Die Ressourcen des {prozess}. Prozess werden freigegeben...")
    for i in range(len(belegt1[0][prozess - 1])):
        re = belegt1[0][prozess - 1].pop(0)
        klasse1.append(re)
    for i in range(len(belegt1[1][prozess - 1])):
        re = belegt1[1][prozess - 1].pop(0)
        klasse2.append(re)
    for i in range(len(belegt1[2][prozess - 1])):
        re = belegt1[2][prozess - 1].pop(0)
        klasse3.append(re)


# print(belegt1) # Nur zur überprüfung- wird später nicht benötigt

def r_vektor():
    global rRessource
    rRessource = [len(klasse1), len(klasse2), len(klasse3)]
    print(f"\nDer Ressourcenrestvektor ist: {rRessource}\n")  # Ausgabe des Ressourcenrestvektors
    logger.info(f"Ressourcenrestvektor ist: {rRessource}\n")
    return rRessource


# Erstellung der Anforderungsmatrix
req = [[], [], []]


# Programm soll selbst entscheiden
def zufall():
    global option
    global wenn_ausgefuehrt
    global wenn_ausgefuehrt2
    global wenn_ausgefuehrt3
    logger.info(f"Der Simulator soll zufällig bestimmen, welcher Prozess ausgeführt werden soll...")
    ressourcen_belegung(option, req)
    freigabe(option)
    if option == 1:
        logger.info(f"Prozess 1 wurde ausgeführt...")
        wenn_ausgefuehrt = True
        option = 0
    elif option == 2:
        logger.info(f"Prozess 2 wurde ausgeführt...")
        wenn_ausgefuehrt2 = True
        option = 0
    elif option == 3:
        logger.info(f"Prozess 3 wurde ausgeführt...")
        wenn_ausgefuehrt3 = True
        option = 0


option = 0


# Die Deadlock Erkennung
def deadlock_erkennung():
    global eingabe
    global option
    global wenn_ausgefuehrt
    global wenn_ausgefuehrt2
    global wenn_ausgefuehrt3
    while True:
        # Überprüft, ob bereits am Anfang ein Deadlock entstanden ist
        if pruefe_deadlock(1) and pruefe_deadlock(2) and pruefe_deadlock(3):
            print("Ein Deadlock ist entstanden")
            logger.info(f"Es ist ein Deadlock entstanden...")
            logger.info(f"Simulator beendet!\n\n ")
            break
        else:
            # Wenn ein Prozess bereits vollendet wurde, wird es nicht mehr angezeigt
            if not pruefe_deadlock(1):
                if not wenn_ausgefuehrt:
                    print(f"Prozess {1} kann durchgeführt werden!")
                    logger.info(f"Prozess {1} kann durchgeführt werden!")
                    option = 1
            if not pruefe_deadlock(2):
                if not wenn_ausgefuehrt2:
                    print(f"Prozess {2} kann durchgeführt werden!")
                    logger.info(f"Prozess {2} kann durchgeführt werden!")
                    option = 2
            if not pruefe_deadlock(3):
                if not wenn_ausgefuehrt3:
                    print(f"Prozess {3} kann durchgeführt werden!")
                    logger.info(f"Prozess {3} kann durchgeführt werden!")
                    option = 3
            time.sleep(1)
            if option == 0:
                print("\nEs ist ein Deadlock entstanden!")
                logger.info(f"Es ist ein Deadlock entstanden...")
                logger.info(f"Simulator beendet!\n\n ")
                break

            if args.input_mode == "s":
                logger.info(f"Abfrage welcher Prozess ausgeführt werden soll...")
                abfrage = int(input('\nWelcher Prozess soll durchgeführt werden? '
                                    '\nWenn das Programm automatisch laufen soll, dann tippen sie "0" ein. '))
                logger.info(f'Es wurde "{abfrage}" ausgewählt...')

                ressourcen_belegung(abfrage, req)
                freigabe(abfrage)
                if not abfrage == 0:
                    ressourcen_belegung(abfrage, req)
                    freigabe(abfrage)
                    if abfrage == 1:
                        logger.info(f"Prozess 1 wurde ausgeführt...")
                        wenn_ausgefuehrt = True
                    elif abfrage == 2:
                        logger.info(f"Prozess 2 wurde ausgeführt...")
                        wenn_ausgefuehrt2 = True
                    elif abfrage == 3:
                        logger.info(f"Prozess 3 wurde ausgeführt...")
                        wenn_ausgefuehrt3 = True
                elif abfrage == 0:
                    zufall()
                    args.input_mode = "d"
                else:
                    "Falsche Eingabe!"

            elif args.input_mode == "d":
                zufall()

        # Wenn kein Programm mehr durchlaufen kann, dann wird ein Deadlock festgestellt
        if r_vektor() == eResource:
            print("\nEs ist kein Deadlock entstanden!")
            logger.info(f"Es ist kein Deadlock entstanden...")
            logger.info(f"Simulator beendet!\n\n ")
            break


def main():
    global req
    logger.info("Simulator startet...")
    mode()

    logger.info("Im Hintergrund werden die benötigten Ressourcen in Listen erstellt...")
    add_ressource(1)
    add_ressource(2)
    add_ressource(3)

    logger.info(f"Belegungsmatrix wird erstellt...")
    # Erstellung der Belegungsmatrix
    alloc = matrix_erstellung("Belegungsmatrix")
    logger.info(f"Belegungsmatrix ist: \n{alloc[0]}\n{alloc[1]}\n{alloc[2]}\n")

    # Einfach nur fürs Design
    print("Ressourcenrestvektor wird berechnet... ")
    logger.info(f"Ressourcenvektor wird berechnet...")
    time.sleep(1)

    # Die Ressourcen der Belegungsmatrix werden belegt
    ressourcen_belegung(1, alloc)
    ressourcen_belegung(2, alloc)
    ressourcen_belegung(3, alloc)

    r_vektor()

    # Erstellung der Anforderungsmatrix
    req = matrix_erstellung("Anforderungsmatrix")
    logger.info(f"Anforderungsmatrix ist: \n{req[0]}\n{req[1]}\n{req[2]}\n")

    deadlock_erkennung()


if __name__ == '__main__':
    main()
