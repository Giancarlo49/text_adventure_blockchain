import module

print("Willkommen zum Adventure")

# Boolean für die Game-Loop
spiel_laeuft = True

#
# Game-Loop
#
while spiel_laeuft:
    # Frage den Benutzer nach der Richtung oder Aktion und konvertiere die Eingabe in Großbuchstaben
    eingabe = input("(N)ord, (O)st, (S)üd, (W)est, (I)nventar, (B)lockchain anzeigen oder Spiel beenden per (Q)uit?").upper()
    print("User-Input:", eingabe)

    # Verarbeite die Benutzereingabe
    match eingabe:
        case "Q":
            # Beende das Spiel
            print("Du beendest das Spiel.")
            spiel_laeuft = False
            
        case "N":
            # Bewegung nach Norden
            result = module.gehe_nord()
            if result == "tueren":
                module.oeffne_tuer()
                
        case "O":
            # Bewegung nach Osten
            result = module.gehe_ost()
            if result == "gegenstand":
                module.waehle_item()
                
        case "S":
            # Bewegung nach Süden
            result = module.gehe_sued()
            if result == "boot":
                module.waehle_boot()
            
        case "W":
            # Bewegung nach Westen
            result = module.gehe_west()
            if result == "ufo":
                module.waehle_ufo()
                
        case "I":
            # Zeige das Inventar
            module.zeige_inventar()

        case "B":
            # Zeige die Blockchain
            module.blockchain.display_chain()

        case _:
            # Ungültige Eingabe
            print("Ich habe das nicht verstanden.")
