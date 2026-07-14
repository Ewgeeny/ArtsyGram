## 1. Collections entfernen

- [x] 1.1 Collection-Modell und Admin-Registrierung entfernen
- [x] 1.2 Vorhandene Collection-Migration bereinigen oder neue Entfernungsmigration anlegen

## 2. Favoriten-Modell einführen

- [x] 2.1 Neues `Favorite`-Modell mit `user`, `post` und `saved_at` erstellen
- [x] 2.2 Eindeutige Relation `unique_together` für User/Post setzen
- [x] 2.3 Migration für das neue Modell erzeugen und anwenden

## 3. Logik und Endpunkte

- [x] 3.1 Toggle-Logik zum Hinzufügen/Entfernen von Favoriten bereitstellen
- [x] 3.2 POST-Endpunkt für das Umschalten eines Favoriten einrichten
- [x] 3.3 GET-Endpunkt für die Profil-Ansicht der Favoritenliste sicherstellen

## 4. UI und Sortierung

- [x] 4.1 Profilansicht um private Favoritenliste ergänzen
- [x] 4.2 Sortierung nach `-saved_at` realisieren
- [x] 4.3 Favoriten-Button/-Aktion für Posts sichtbar machen

## 5. Prüfung

- [x] 5.1 Bestehende Tests aktualisieren oder ergänzen
- [x] 5.2 Migration und App-Laufzeit prüfen
