## Why

Der aktuelle Collections-Ansatz passt nicht zum geplanten Nutzerfluss. Stattdessen wird eine private Favoritenliste gebraucht, mit der Nutzer*innen Posts speichern und auf ihrem Profil nach Speicherzeit sortiert anzeigen lassen können.

## What Changes

- Entfernt die bisherige Collection-Funktionalität aus Modell, Admin und zugehöriger Logik.
- Führt eine neue Favorite-Entität als private, nutzerbezogene Sammlung ein.
- Ermöglicht das Speichern und Entfernen von Posts als Favorit.
- Zeigt im Profil eine private Favoritenliste an, sortiert nach zuletzt gespeicherten Einträgen zuerst.

## Capabilities

### New Capabilities

- `favorites-private-list`: Private Favoritenliste mit Hinzufügen/Entfernen und Profilansicht, sortiert nach Speicherzeit (neueste Zuerst).

### Modified Capabilities

- `collections-removal`: Entfernt die bisherige Collection-Funktionalität aus UI und Logik.

## Impact

- Betroffener Code: Models, Admin, Views, Templates, Formulare und URL-Routing rund um Collections/Favorites.
- Datenmigration: Vorhandene Collection-Daten müssen bewertet und ggf. migriert oder entfernt werden.
- Nebenwirkungen: Bestehende Collection-Links/Features werden entfernt und durch Profil-Favoriten ersetzt.
