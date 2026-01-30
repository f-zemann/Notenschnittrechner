
def anzahl_noten():
    """
    Fragt den Benutzer nach der Anzahl der Noten.
    Gibt None zurück, wenn der Vorgang mit 0 abgebrochen wird.
    """
    print('Abbruch mit 0')

    while True:
        try:
            anzahl = int(input('Wie viele Noten möchtest du eintragen?\n'))
        except ValueError:
            print('Bitte gültige Zahl eingeben')
            continue

        # Abbruchsignal für das gesamte Programm
        if anzahl == 0:
            return None

        return anzahl


def noteneingabe(anzahl, liste):
    """
    Fragt genau 'anzahl' gültige Noten (1–6) ab.
    Ungültige Eingaben zählen nicht als Versuch.
    Abbruch mit 0 beendet die Eingabe frühzeitig.
    """
    print('Abbruch mit 0')
    count = 0

    # Zählt nur erfolgreich eingegebene Noten
    while count < anzahl:
        try:
            note = int(input(f'Note {count + 1}: '))
        except ValueError:
            print('Bitte Ganzzahlen von 1–6 eingeben.')
            continue

        # Globaler Abbruch der Eingabe
        if note == 0:
            return

        # Bereichsprüfung der Note
        if note < 1 or note > 6:
            print('Bitte Ganzzahlen von 1–6 eingeben.')
            continue

        liste.append(note)
        count += 1


def durchschnittsrechner(liste):
    """
    Berechnet den Durchschnitt der Notenliste.
    Gibt None zurück, wenn keine Noten vorhanden sind.
    """
    if len(liste) > 0:
        return sum(liste) / len(liste)

    return None


def ausgabe(liste, durchschnitt):
    """
    Gibt die erfassten Noten und den berechneten Durchschnitt aus.
    """
    if len(liste) == 0:
        print('Keine Noten vorhanden.')
    else:
        print("Deine Noten sind:", *liste, sep=" ")

    if durchschnitt is None:
        print('Durchschnitt konnte nicht berechnet werden.')
    else:
        print(f"Dein Notendurchschnitt ist: {durchschnitt:.2f}")


def notenerfassen():
    """
    Steuert den gesamten Ablauf:
    Eingabe → Verarbeitung → Ausgabe
    """
    noten = []

    anzahl = anzahl_noten()
    if anzahl is None:
        print('Vorgang frühzeitig abgebrochen.')
        return

    noteneingabe(anzahl, noten)
    durchschnitt = durchschnittsrechner(noten)
    ausgabe(noten, durchschnitt)


notenerfassen()
