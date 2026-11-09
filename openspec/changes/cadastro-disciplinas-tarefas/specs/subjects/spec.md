# Spec Delta

## MODIFIED Requirements

### Requirement: Frontend integration for subjects in EduTrack AI
The frontend application SHALL display registered subjects under "Disciplinas" synchronized with Xano for the authenticated user, provide an interface for adding new subjects, and reflect the count of active subjects on the "Dashboard" metric.

#### Scenario: View active subjects metric on Dashboard
- **WHEN** user views the Dashboard
- **THEN** the "Disciplinas Ativas" metric displays the count of active subjects

#### Scenario: Add and list subjects in Disciplinas view
- **WHEN** user opens the "Disciplinas" view with an active authentication session
- **THEN** the system displays all enrolled subjects retrieved from Xano and provides a form to add a new subject

#### Scenario: Unauthenticated access to Disciplinas view
- **WHEN** user opens the "Disciplinas" view without being logged in
- **THEN** the system SHALL present an informative warning directing the user to log in on the profile page

