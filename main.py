

import json                      # Speichert Daten in einer Datei
import hashlib                   # Macht Passwörter sicher (Hashing)
import os                        # Prüft Dateien / arbeitet mit System

# Dateiname für unsere gespeicherten Passwörter
DATA_FILE = "passwords.json"


# Funktion: Passwort hashen (Sicher speichern)
def hash_password(password):
    """
    Diese Funktion nimmt ein Passwort als Text und wandelt es in einen sicheren Hash um.
    So speichern wir niemals das echte Passwort.
    """
    return hashlib.sha256(password.encode()).hexdigest()


# Funktion: Datei laden oder neu erstellen
def load_data():
    """
    Diese Funktion lädt die JSON Datei.
    Falls sie noch nicht existiert, wird sie neu erstellt.
    """
    if not os.path.exists(DATA_FILE):
        # Falls Datei nicht existiert → neue Struktur erstellen
        with open(DATA_FILE, "w") as file:
            json.dump({"master_password": "", "passwords": {}}, file)

    with open(DATA_FILE, "r") as file:
        return json.load(file)


# Funktion: Daten speichern
def save_data(data):
    """
    Speichert unsere Daten wieder in die JSON Datei.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Funktion: Master Passwort setzen (erstes Mal)
def setup_master_password(data):
    """
    Wenn noch kein Master Passwort existiert, wird hier eines gesetzt.
    """
    print("Erstelle ein Master Passwort:")
    master_password = input("Neues Master Passwort: ")

    # Passwort wird gehashed gespeichert
    data["master_password"] = hash_password(master_password)
    save_data(data)

    print("Master Passwort gespeichert!")


# Funktion: Login prüfen
def verify_master_password(data):
    """
    Überprüft ob das eingegebene Passwort mit dem gespeicherten Hash übereinstimmt.
    """
    master_password = input("Master Passwort eingeben: ")

    if hash_password(master_password) == data["master_password"]:
        return True
    else:
        print("Falsches Passwort!")
        return False


# Funktion: Neues Passwort hinzufügen
def add_password(data):
    """
    Speichert ein neues Passwort für eine Website.
    """
    website = input("Website Name: ")
    username = input("Username: ")
    password = input("Passwort: ")

    data["passwords"][website] = {
        "username": username,
        "password": password
    }

    save_data(data)
    print("Passwort gespeichert!")


# Funktion: Passwörter anzeigen
def view_passwords(data):
    """
    Zeigt alle gespeicherten Passwörter an.
    """
    if not data["passwords"]:
        print("Keine Passwörter gespeichert.")
        return

    for website, info in data["passwords"].items():
        print("\n-------------------")
        print(f"Website: {website}")
        print(f"Username: {info['username']}")
        print(f"Passwort: {info['password']}")


# Hauptprogramm
def main():
    """
    Hauptlogik des Programms.
    Hier startet alles.
    """

    data = load_data()

    # Falls noch kein Master Passwort existiert
    if data["master_password"] == "":
        setup_master_password(data)

    # Login prüfen
    if not verify_master_password(data):
        return

    # Menü
    while True:
        print("\n--- Passwort Manager ---")
        print("1 - Passwort hinzufügen")
        print("2 - Passwörter anzeigen")
        print("3 - Beenden")

        choice = input("Auswahl: ")

        if choice == "1":
            add_password(data)
        elif choice == "2":
            view_passwords(data)
        elif choice == "3":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe!")


# Programm starten
if __name__ == "__main__":
    main()
