from blockchain import Blockchain

# Initialisiere die Blockchain
blockchain = Blockchain()

# HP des Helden
hero_hp = 100

# Inventar des Helden
inventar = ["Apfel", "Holzschwert", "Ring"]

# Funktionen *********************************************************************

# Funktion für Bewegung nach Norden
def gehe_nord():
    global hero_hp  # Zugriff auf die globale Variable hero_hp
    print("Du gehst nach Norden.")
    hero_hp -= 1  # Verringere die Lebenspunkte um 1
    print("Aktuelle HP:", hero_hp)
    blockchain.add_block("Der Spieler ging nach Norden. HP: " + str(hero_hp))  # Ereignis zur Blockchain hinzufügen
    return "tueren"

# Funktion für Bewegung nach Süden
def gehe_sued():
    global hero_hp
    print("Du gehst nach Süden.")
    hero_hp -= 1
    print("Aktuelle HP:", hero_hp)
    blockchain.add_block("Der Spieler ging nach Süden. HP: " + str(hero_hp))
    return "boot"

# Funktion für Bewegung nach Westen
def gehe_west():
    global hero_hp
    print("Du gehst nach Westen.")
    hero_hp -= 1
    print("Aktuelle HP:", hero_hp)
    blockchain.add_block("Der Spieler ging nach Westen. HP: " + str(hero_hp))
    return "ufo"

# Funktion für Bewegung nach Osten
def gehe_ost():
    global hero_hp
    print("Du gehst nach Osten.")
    hero_hp -= 1
    print("Aktuelle HP:", hero_hp)
    blockchain.add_block("Der Spieler ging nach Osten. HP: " + str(hero_hp))
    return "gegenstand"

# Funktion zum Anzeigen des Inventars
def zeige_inventar():
    print("Du schaust ins Inventar. Dort findest Du:")
    for gegenstand in inventar:
        print("\t -", gegenstand.upper())  # Zeigt jedes Item im Inventar in Großbuchstaben an
    print("Insgesamt:", len(inventar))
    blockchain.add_block("Spieler hat das Inventar überprüft. Inventar: " + str(inventar))

# Türen im Norden ************************************************************************

# Funktion zum Öffnen einer Tür
def oeffne_tuer():
    global hero_hp, inventar  # Zugriff auf die globalen Variablen
    print("Du stehst vor drei Türen: Tür 1, Tür 2 und Tür 3.")
    print("Welche Tür möchtest du öffnen?")
    tuer = input("Wähle 1, 2 oder 3: ")
    match tuer:
        case "1":
            print("Du hast eine Schatzkiste gefunden!")
            hero_hp += 10
            print("Du hast 10 HP erhalten. Aktuelle HP:", hero_hp)
            blockchain.add_block("Spieler öffnete Tür 1 und fand eine Schatzkiste. HP: " + str(hero_hp))
        case "2":
            print("Oh nein, ein Monster! Wähle eine Waffe aus deinem Inventar, um es zu bekämpfen:")
            print(", ".join(inventar))  # Zeigt die verfügbaren Gegenstände im Inventar
            waffe = input("Gib den Namen der Waffe ein, die du verwenden möchtest: ")
            if waffe.lower() == "armbrust":
                print("Du benutzt die Armbrust, um das Monster zu erledigen. Gut gemacht!")
                print("Das Monster wurde erfolgreich erledigt!")
                hero_hp += 20  # Belohnung für das Erlegen des Monsters
                print("Du erhältst 20 HP. Aktuelle HP:", hero_hp)
                blockchain.add_block("Spieler besiegte das Monster mit einer Armbrust. HP: " + str(hero_hp))
            else:
                print("Deine Waffe hat keine Wirkung auf das Monster. Es greift dich an!")
                hero_hp -= 10
                print("Du verlierst 10 HP. Aktuelle HP:", hero_hp)
                blockchain.add_block("Spieler konnte das Monster nicht besiegen. HP: " + str(hero_hp))
        case "3":
            print("Der Raum ist leer, nichts passiert.")
            print("Aktuelle HP:", hero_hp)
            blockchain.add_block("Spieler öffnete Tür 3, der Raum war leer. HP: " + str(hero_hp))
        case _:
            print("Eingabe ungültig. Du stehst noch vor den drei Türen.")

# Gegenstände im Osten ************************************************************************

# Funktion zum Auswählen eines Gegenstands
def waehle_item():
    global hero_hp, inventar
    print("Du stehst in der Wüste vor einem Karren.")
    print("Auf dem Karren befinden sich drei Gegenstände: Öllampe, Große Kiste und Tonkrug.")
    gegenstand = input("Wähle: (O)ellampe, (K)iste oder (T)onkrug: ")
    match gegenstand.upper():
        case "O":
            print("Du reibst an der Lampe... Nichts passiert.")
            hero_hp -= 5
            print("Du verlierst 5 HP.", hero_hp)
            blockchain.add_block("Spieler wählte die Öllampe, nichts passierte. HP: " + str(hero_hp))
        case "K":
            print("In der Kiste befinden sich eine Armbrust mit Pfeilen und ein Heiltrank.")
            print("Du trinkst den Heiltrank und die Armbrust wurde deinem Inventar hinzugefügt.")
            inventar.append("Armbrust")
            hero_hp += 15
            print("Du hast 15 HP erhalten. Aktueller HP:", hero_hp)
            blockchain.add_block("Spieler wählte die Kiste, erhielt eine Armbrust und Heiltrank. HP: " + str(hero_hp) + ", Inventar: " + str(inventar))
        case "T":
            print("Im Tonkrug ist Wasser. Du trinkst es und erhälst 1 HP")
            hero_hp += 1
            print("Aktueller HP:", hero_hp)
            blockchain.add_block("Spieler wählte den Tonkrug und erhielt 1 HP. HP: " + str(hero_hp))
        case _:
            print("Eingabe ungültig. Wähle einen Gegenstand")

# Boote im Süden ****************************************************************************************

# Funktion zum Auswählen eines Boots
def waehle_boot():
    global hero_hp, inventar
    print("Du kommst an einem Strand und am Horizont ist eine kleine Insel zu erkennen.")
    print("Am Strand liegen ein Schlauchboot, ein kleines Fischerboot und ein angeschwemmter Rettungsring.")

    # Wiederholt sich bis das Fischerboot gewählt wird
    while True:
        boot = input("Wähle: (S)chlauchboot, (F)ischerboot oder (R)ettungsring um die Insel zu erreichen: ")
        match boot.upper():
            case "S":
                print("Du kommst 50 Meter weit und musst zurück schwimmen. Dem Schlauchboot ist die Luft entwichen!")
                hero_hp -= 10
                print("Du verlierst 10 HP. Aktueller HP:", hero_hp)
                blockchain.add_block("Spieler wählte das Schlauchboot, es verlor Luft. HP: " + str(hero_hp))
            case "F":
                print("Du erreichst wohlbehalten die einsame Insel. Sie ist üppig an Kokospalmen.")
                print("Du ernährst dich gut und fährst wieder zurück. Eine Kokosnuss nimmst du mit.")
                inventar.append("Kokosnuss")
                hero_hp += 15
                print("Du erhältst 15 HP. Aktueller HP:", hero_hp)
                blockchain.add_block("Spieler wählte das Fischerboot und erreichte die Insel. HP: " + str(hero_hp) + ", Inventar: " + str(inventar))
                return  # Beendet die Schleife, wenn das Fischerboot ausgewählt wurde (while True:)
            case "R":
                print("Du benutzt den Rettungsring und schwimmst zur Insel. Auf halber Strecke wirst du von einem Hai attackiert und verlierst 25 HP")
                hero_hp -= 25
                print("Aktueller HP:", hero_hp)
                blockchain.add_block("Spieler wählte den Rettungsring und wurde von einem Hai attackiert. HP: " + str(hero_hp))
            case _:
                print("Eingabe ungültig. Wähle noch einmal.")

# UFOs im Westen ***************************************************************************************

# Funktion zum Auswählen eines UFOs
def waehle_ufo():
    global hero_hp, inventar
    print("Du erreichst eine futuristische Startbahn.")
    print("Dort stehen drei UFOs mit verschiedenen Aufschriften:")

    # Wiederholt sich bis Innererde gewählt wird
    while True:
        ufo = input("Wähle: 1 für Mond, 2 für Mars und 3 für Innererde: ")
        match ufo.upper():
            case "1":
                print("Du fliegst zum Mond. Doch noch rechtzeitig bemerkst du, der Mond ist Plasma und du kannst nicht darauf landen.")
                print("Du fliegst zurück und verlierst 2 HP.")
                hero_hp -= 2
                print("Aktueller HP:", hero_hp)
                blockchain.add_block("Spieler wählte das UFO zum Mond. Der Mond war Plasma. HP: " + str(hero_hp))
            case "2": 
                print("Du fliegst zum Mars. Leider stößt du immer wieder gegen das Firmament.")
                print("Dein UFO ist schwer beschädigt und du fliegst zurück. Du verlierst 5 HP.")
                hero_hp -= 5
                print("Aktueller HP:", hero_hp)
                blockchain.add_block("Spieler wählte das UFO zum Mars. Stieß gegen das Firmament. HP: " + str(hero_hp))
            case "3":
                print("Du fliegst zur Innererde durch den Einstieg am Nordpol.")
                print("Du wirst von den blauen Menschen herzlich empfangen.")
                print("Sie erfüllen dich mit Weisheit und Liebe. Du erhältst Pflanzensamen und 50 HP.")
                inventar.append("Pflanzensamen")
                hero_hp += 50
                print("Aktueller HP:", hero_hp)
                blockchain.add_block("Spieler wählte das UFO zur Innererde. Erhielt Weisheit, Liebe und Pflanzensamen. HP: " + str(hero_hp) + ", Inventar: " + str(inventar))
                return  # Beendet die Schleife, wenn Innererde ausgewählt wurde (while True:)
