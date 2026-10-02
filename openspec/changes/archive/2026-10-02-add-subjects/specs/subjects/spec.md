# Spec Delta

## Purpose

Provides academic subject (disciplina) management for students, including subject registration, listing, detail viewing, updating, and archiving/deletion.

## ADDED Requirements

### Requirement: User can list their subjects
The system SHALL allow users to list all their registered subjects with optional filtering by status (e.g., active, completed, archived).

#### Scenario: Retrieve active subjects list
- **WHEN** user requests their list of subjects
- **THEN** system returns a collection of subjects belonging to the user, including id, name, code, professor, semester, and status

### Requirement: User can create a new subject
The system SHALL allow users to register a new academic subject by specifying a name, along with optional course code, professor name, and academic period/semester.

#### Scenario: Successfully create subject with valid data
- **WHEN** user submits subject details with a non-empty name
- **THEN** system creates the subject with status "active" and returns the saved subject record with its generated identifier

#### Scenario: Validation failure on missing name
- **WHEN** user attempts to create a subject without providing a name
- **THEN** system rejects the request with an appropriate validation error

### Requirement: User can retrieve details of a subject
The system SHALL allow users to retrieve the full information for a specific subject by its ID.

#### Scenario: Retrieve existing subject details
- **WHEN** user requests details for an existing subject ID belonging to their account
- **THEN** system returns the full subject data record

### Requirement: User can update an existing subject
The system SHALL allow users to modify editable fields of an existing subject (name, code, professor, semester, or status).

#### Scenario: Successfully update subject details
- **WHEN** user submits updated fields for an existing subject they own
- **THEN** system saves the modifications and returns the updated subject record

### Requirement: User can delete or archive a subject
The system SHALL allow users to delete or mark an existing subject as archived.

#### Scenario: Delete an existing subject
- **WHEN** user requests deletion of a subject they own
- **THEN** system removes or archives the subject and confirms completion

### Requirement: Frontend integration for subjects in EduTrack AI
The frontend application SHALL display registered subjects under "Disciplinas", provide an interface for adding new subjects, and reflect the count of active subjects on the "Dashboard" metric.

#### Scenario: View active subjects metric on Dashboard
- **WHEN** user views the Dashboard
- **THEN** the "Disciplinas Ativas" metric displays the count of active subjects

#### Scenario: Add and list subjects in Disciplinas view
- **WHEN** user opens the "Disciplinas" view
- **THEN** the system displays all enrolled subjects and provides a form to add a new subject

