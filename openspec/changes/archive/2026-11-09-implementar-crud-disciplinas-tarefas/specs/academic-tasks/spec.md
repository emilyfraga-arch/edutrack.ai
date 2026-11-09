# Spec Delta

## Purpose

Enables students in EduTrack AI to record, track, and manage academic tasks and deadlines linked to their subjects via authenticated CRUD operations with strict data isolation.

## ADDED Requirements

### Requirement: User can list their academic tasks
The system SHALL allow authenticated users to list all their academic tasks, strictly filtering records to return only tasks where user_id matches the authenticated user ($auth.id).

#### Scenario: Retrieve tasks for authenticated user
- **WHEN** user requests their list of academic tasks with a valid authentication token
- **THEN** system returns a collection of tasks belonging strictly to that user, including id, title, description, due_date, status, subject_id, and created_at

#### Scenario: Unauthenticated request rejected
- **WHEN** a client requests the tasks list without a valid authentication token
- **THEN** system SHALL reject the request with HTTP 401 Unauthorized

### Requirement: User can create a new academic task
The system SHALL allow authenticated users to create a new academic task specifying title, optional description, due date, status, and subject_id, automatically associating user_id with the authenticated user ($auth.id) and ignoring any client-supplied user_id.

#### Scenario: Successfully create task with valid data
- **WHEN** user submits task details with a non-empty title and a valid authentication token
- **THEN** system creates the task with user_id set to the authenticated user ID and returns the created task record

#### Scenario: Validation failure on missing title
- **WHEN** user attempts to create a task without providing a title
- **THEN** system rejects the request with an appropriate validation error

### Requirement: User can retrieve details of an academic task
The system SHALL allow users to retrieve the full information for a specific academic task by its ID, enforcing that the record belongs to the authenticated user ($auth.id).

#### Scenario: Retrieve existing task details owned by user
- **WHEN** user requests details for an existing task ID belonging to their account
- **THEN** system returns the full academic task data record

#### Scenario: Unauthorized access to task owned by another user
- **WHEN** user attempts to retrieve details for a task ID belonging to another user
- **THEN** system SHALL return a 404 Not Found error

### Requirement: User can update an existing academic task
The system SHALL allow authenticated users to modify editable fields of an existing task (title, description, due_date, status, subject_id), enforcing that the record belongs to the authenticated user ($auth.id).

#### Scenario: Successfully update task details or status
- **WHEN** user submits updated fields for an existing task they own
- **THEN** system saves the modifications and returns the updated task record

#### Scenario: Reject update for task owned by another user
- **WHEN** user attempts to update a task ID belonging to another user
- **THEN** system SHALL return a 404 Not Found error

### Requirement: User can delete an academic task
The system SHALL allow authenticated users to delete an existing academic task, enforcing that the record belongs to the authenticated user ($auth.id).

#### Scenario: Delete an existing task owned by user
- **WHEN** user requests deletion of a task they own
- **THEN** system removes the task and confirms completion

#### Scenario: Reject deletion of task owned by another user
- **WHEN** user attempts to delete a task ID belonging to another user
- **THEN** system SHALL return a 404 Not Found error

### Requirement: Frontend integration for academic tasks in EduTrack AI
The frontend application SHALL display registered tasks under "Tarefas" synchronized with Xano for the authenticated user, allow filtering by status and search text, allow toggling task status, provide an interface for adding new tasks linked to subjects, and provide options to delete tasks.

#### Scenario: List and filter tasks in Tarefas view
- **WHEN** user opens the "Tarefas" view with an active authentication session
- **THEN** the system displays tasks retrieved from Xano and applies search and status filters

#### Scenario: Add a new task in Tarefas view
- **WHEN** user submits a new task form with title, optional subject, description, and due date
- **THEN** the system sends the task to Xano and refreshes the list upon success

#### Scenario: Toggle task completion status
- **WHEN** user toggles the completion checkbox for a task
- **THEN** the system updates the status in Xano and refreshes the view

