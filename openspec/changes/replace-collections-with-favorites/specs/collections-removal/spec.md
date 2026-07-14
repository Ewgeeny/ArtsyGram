## ADDED Requirements

### Requirement: Remove collections feature
Das System SHALL die bisherige Collection-Funktionalität vollständig entfernen.

#### Scenario: No collection UI or logic remains
- **WHEN** die App genutzt wird
- **THEN** gibt es keine Collections-Mehr, keine zugehörigen Routes, Views oder Modelle mehr

### Requirement: Clean up migration history
Das System SHALL die bisherige Collection-Migration und Modeldefinition sicher entfernen.

#### Scenario: Migration state is consistent
- **WHEN** die Datenbank nach der Änderung geprüft wird
- **THEN** existiert kein Collection-Modell mehr und es gibt inkonsistente Migrationen nicht
