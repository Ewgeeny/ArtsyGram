## ADDED Requirements

### Requirement: User can save post to private favorites
Das System SHALL es Nutzer*innen erlauben, einen Post zur eigenen Favoritenliste hinzuzufügen.

#### Scenario: Save a post as favorite
- **WHEN** eine Nutzerin/ein Nutzer einen Post als Favorit markiert
- **THEN** wird der Post in dessen private Favoritenliste übernommen

### Requirement: User can remove post from private favorites
Das System SHALL es Nutzer*innen erlauben, einen Post aus der eigenen Favoritenliste zu entfernen.

#### Scenario: Remove a post from favorites
- **WHEN** eine Nutzerin/ein Nutzer einen Favoriten entfernt
- **THEN** wird der Post aus dessen Favoritenliste gelöscht

### Requirement: Profile shows own favorites sorted by newest saved first
Das System SHALL die eigene Favoritenliste im Profil sortiert nach Speicherzeit anzeigen, zuletzt gespeichert zuerst.

#### Scenario: Favorites order on profile
- **WHEN** die Profilseite mit Favoriten aufgerufen wird
- **THEN** werden die Einträge in der Reihenfolge neueste Speicherzeit zuerst angezeigt

### Requirement: Favorites list is private
Das System SHALL die Favoritenliste nur für die eigene Nutzerin/den eigenen Nutzer sichtbar machen.

#### Scenario: Other users cannot view favorites
- **WHEN** eine fremde Nutzerin/ein fremder Nutzer das Profil aufruft
- **THEN** werden keine Favoriten angezeigt
