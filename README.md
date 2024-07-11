# Text Adventure Spiel mit Blockchain

Dieses Projekt ist ein einfaches Text-Adventure-Spiel, das eine Blockchain zur Aufzeichnung von Spielereignissen verwendet. Es besteht aus drei Hauptkomponenten: dem Spielskript (`text_adv_geruest.py`), der Blockchain-Implementierung (`blockchain.py`) und den Modulen für die Spielmechanik (`module.py`).

## Anforderungen

- Python 3.x
- Ein Modul namens `module` (dieses Modul ist Teil des Projekts)

## Installation

1. Stellen Sie sicher, dass Python 3.x auf Ihrem System installiert ist. Sie können die neueste Version von [Python.org](https://www.python.org/) herunterladen.

2. Platzieren Sie die folgenden Dateien im gleichen Verzeichnis:
   - `text_adv_geruest.py`
   - `blockchain.py`
   - `module.py`

## Nutzung

1. Führen Sie das Hauptskript `text_adv_geruest.py` aus:

   ```sh
   python text_adv_geruest.py
   ```

2. Befolgen Sie die Anweisungen im Spiel, um sich in verschiedene Richtungen zu bewegen, das Inventar anzuzeigen, die Blockchain anzuzeigen oder das Spiel zu beenden.

## Spielsteuerung

- `(N)ord`: Bewegung nach Norden
- `(O)st`: Bewegung nach Osten
- `(S)üd`: Bewegung nach Süden
- `(W)est`: Bewegung nach Westen
- `(I)nventar`: Zeige das Inventar
- `(B)lockchain anzeigen`: Zeige die Blockchain
- `(Q)uit`: Spiel beenden

## Dateibeschreibungen

### text_adv_geruest.py

Dies ist das Hauptspielskript, das die Spielschleife enthält und Benutzereingaben verarbeitet, um entsprechende Aktionen auszuführen.

### blockchain.py

Dieses Skript enthält die Implementierung der Blockchain. Es definiert die `Block`- und `Blockchain`-Klassen und stellt Funktionen zum Erstellen und Verifizieren der Blockchain zur Verfügung.

### module.py

Dieses Modul enthält die Funktionen für die Bewegungen und Aktionen des Spielers im Spiel. Es integriert die Blockchain, um Ereignisse wie Bewegungen und Interaktionen aufzuzeichnen.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der [LICENSE](LICENSE)-Datei.
