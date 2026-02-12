
Dieser Passwort-Manager ist eine Kommandozeilenanwendung (CLI), die ich mit Python entwickelt habe. 
Mit dem Programm kann man Login-Daten für verschiedene Websites speichern und verwalten. 

Beim ersten Start wird ein Master-Passwort festgelegt, das nicht im Klartext gespeichert wird. 
Stattdessen wird es mit dem SHA256-Algorithmus gehashed und als Hash-Wert in einer JSON-Datei abgelegt. 
Beim späteren Login wird das eingegebene Passwort ebenfalls gehashed und mit dem gespeicherten Wert verglichen, 
um die Authentifizierung durchzuführen.

Die Zugangsdaten bestehen aus Website, Benutzername und Passwort und werden strukturiert 
in einer JSON-Datei gespeichert. Dadurch bleiben die Daten auch nach dem Beenden 
des Programms erhalten.

Das Projekt zeigt grundlegende Konzepte wie:
- Datei-Handling in Python
- Arbeiten mit JSON-Daten
- Nutzung von Hash-Funktionen (SHA256)
- Strukturierter Aufbau eines CLI-Programms
- Benutzerinteraktion über ein textbasiertes Menü

Ziel des Projekts war es, ein praktisches Tool zu entwickeln und gleichzeitig 
ein besseres Verständnis für Datenspeicherung, Programmstruktur und 
grundlegende Sicherheitsmechanismen zu bekommen.
