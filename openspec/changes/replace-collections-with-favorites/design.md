## Context

Die App besitzt aktuell eine Collection-Funktionalität, die nicht dem gewünschten Nutzerfluss entspricht. Es wird stattdessen eine private Favoristenliste benötigt, die auf dem Profil nach Speicherzeit sortiert angezeigt wird.

## Goals / Non-Goals

**Goals:**
- Ermöglicht das Speichern und Entfernen von Posts als Favorit.
- Stellt eine private Profilansicht bereit, die nur eigene Favoriten anzeigt.
- Sortiert Favoriten nach Speicherzeit, zuletzt gespeichert zuerst.
- Entfernt die bisherige Collection-Funktionalität sauber aus UI und Logik.

**Non-Goals:**
- Keine öffentlichen Sammlungen oder Sharing-Funktionen für Favoriten.
- Keine separaten Ordner/Tags innerhalb der Favoriten.
- Keine Wiederherstellung alter Collection-Daten, sofern nicht explizit angefordert.

## Decisions

- Neues Modell `Favorite` mit `user`, `post` und `saved_at` statt allgemeiner Collection-Struktur.
- Eindeutige Relation `unique_together` pro User/Post, damit kein Duplikat entsteht.
- Favoriten über POST-Endpunkte umschaltbar machen und Profilansicht über GET anzeigen.
- Sortierung in der Profilansicht über `-saved_at`, um neueste Einträge zuerst zu zeigen.
- Collection-Modell, Admin-Eintrag und zugehörige Ansichten werden entfernt.

## Risks / Trade-offs

- [Datenverlust alter Collections] → Migration prüfen; wenn keine Nutzdaten relevant sind, klar dokumentieren.
- [Verwirrung durch Feature-Wechsel] → UI-Hinweise auf Favoriten statt Collections einsetzen.
- [Doppelte Klicks/Status] → Toggle-Logik mit Eindeutigkeitsregel absichern.
