import hashlib
import time

# Klasse für einen Block in der Blockchain
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index  # Index des Blocks in der Kette
        self.previous_hash = previous_hash  # Hash des vorherigen Blocks
        self.timestamp = timestamp  # Zeitpunkt der Erstellung des Blocks
        self.data = data  # Daten, die im Block gespeichert sind
        self.hash = hash  # Hash des aktuellen Blocks

# Funktion zur Berechnung des Hashes eines Blocks
def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

# Funktion zur Erstellung des Genesis-Blocks (erster Block in der Blockchain)
def create_genesis_block():
    timestamp = int(time.time())
    return Block(0, "0", timestamp, "Genesis Block", calculate_hash(0, "0", timestamp, "Genesis Block"))

# Funktion zur Erstellung eines neuen Blocks basierend auf dem vorherigen Block
def create_new_block(previous_block, data):
    index = previous_block.index + 1  # Index des neuen Blocks
    timestamp = int(time.time())  # Zeitpunkt der Erstellung des neuen Blocks
    hash = calculate_hash(index, previous_block.hash, timestamp, data)  # Berechnung des Hashes für den neuen Block
    return Block(index, previous_block.hash, timestamp, data, hash)

# Klasse für die Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]  # Initialisiere die Blockchain mit dem Genesis-Block

    # Funktion zur Rückgabe des letzten Blocks in der Kette
    def get_latest_block(self):
        return self.chain[-1]

    # Funktion zum Hinzufügen eines neuen Blocks zur Blockchain
    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = create_new_block(previous_block, data)
        self.chain.append(new_block)

    # Funktion zur Überprüfung der Gültigkeit der Blockchain
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Überprüfung, ob der Hash des aktuellen Blocks korrekt ist
            if current_block.hash != calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False

            # Überprüfung, ob der vorherige Hash des aktuellen Blocks mit dem Hash des vorherigen Blocks übereinstimmt
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    # Funktion zur Anzeige der gesamten Blockchain
    def display_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print("-" * 30)
