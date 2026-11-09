# subjects Specification

## Purpose
Provides academic subject (disciplina) management for students, including subject registration, listing, detail viewing, updating, and archiving/deletion.

## Requirements

### Requirement: User can list their subjects
The system SHALL allow users to list all their registered subjects with optional filtering by status, strictly filtering records to return only subjects where user_id matches the authenticated user ($auth.id).

#### Scenario: Retrieve active subjects list
- **WHEN** user requests their list of subjects with a valid authentication token
- **THEN** system returns a collection of subjects belonging strictly to that user, including id, name, code, professor, semester, and status

#### Scenario: Unauthenticated request rejected
- **WHEN** a client requests the subjects list without a valid authentication token
- **THEN** system SHALL reject the request with HTTP 401 Unauthorized

### Requirement: User can create a new subject
The system SHALL allow users to register a new academic subject by specifying a name, along with optional course code, professor name, and academic period/semester, automatically associating user_id with the authenticated user ($auth.id) and ignoring any client-supplied user_id.

#### Scenario: Successfully create subject with valid data
- **WHEN** user submits subject details with a non-empty name and a valid authentication token
- **THEN** system creates the subject with user_id set to the authenticated user ID and returns the created subject record

#### Scenario: Validation failure on missing name
- **WHEN** user attempts to create a subject without providing a name
- **THEN** system rejects the request with an appropriate validation error

### Requirement: User can retrieve details of a subject
The system SHALL allow users to retrieve the full information for a specific subject by its ID, enforcing that the record belongs to the authenticated user ($auth.id).

#### Scenario: Retrieve existing subject details
- **WHEN** user requests details for an existing subject ID belonging to their account
- **THEN** system returns the full subject data record

#### Scenario: Unauthorized access to subject owned by another user
- **WHEN** user attempts to retrieve details for a subject ID belonging to another user
- **THEN** system SHALL return a 404 Not Found error

### Requirement: User can update an existing subject
The system SHALL allow users to modify editable fields of an existing subject (name, code, professor, semester), enforcing that the record belongs to the authenticated user ($auth.id).

#### Scenario: Successfully update subject details
- **WHEN** user submits updated fields for an existing subject they own
- **THEN** system saves the modifications and returns the updated subject record

#### Scenario: Reject update for subject owned by another user
- **WHEN** user attempts to update a subject ID belonging to another user
- **THEN** system SHALL return a 404 Not Found error

### Requirement: User can delete or archive a subject
The system SHALL allow users to delete or mark an existing subject as archived, enforcing that the record belongs to the authenticated user ($auth.id).

#### Scenario: Delete an existing subject
- **WHEN** user requests deletion of a subject they own
- **THEN** system removes or archives the subject and confirms completion

#### Scenario: Reject deletion of subject owned by another user
- **WHEN** user attempts to delete a subject ID belonging to another user
- **THEN** system SHALL return a 404 Not Found error

### Requirement: Frontend integration for subjects in EduTrack AI
The frontend application SHALL display registered subjects under "Disciplinas" synchronized with Xano for the authenticated user, provide an interface for adding new subjects and deleting existing ones, and reflect the count of active subjects on the "Dashboard" metric.

#### Scenario: View active subjects metric on Dashboard
- **WHEN** user views the Dashboard
- **THEN** the "Disciplinas Ativas" metric displays the count of active subjects

#### Scenario: Add and list subjects in Disciplinas view
- **WHEN** user opens the "Disciplinas" view with an active authentication session
- **THEN** the system displays all enrolled subjects retrieved from Xano, provides a form to add a new subject, and allows deleting registered subjects
