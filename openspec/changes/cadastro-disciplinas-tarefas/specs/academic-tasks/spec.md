# academic-tasks Specification

## Purpose
Allows authenticated students to list, register, filter, and track academic tasks associated with their enrolled subjects in Xano through EduTrack AI.

## ADDED Requirements

### Requirement: List academic tasks for authenticated user
The system SHALL retrieve all academic tasks belonging to the authenticated user from the Xano `academic_tasks` table and display them in the tasks interface.

#### Scenario: User views list of academic tasks
- **WHEN** an authenticated user accesses the "Minhas Tarefas" page
- **THEN** the system SHALL send a GET request to `/academic_tasks` with the Bearer token and render each task with title, associated subject, due date, and status

#### Scenario: User is unauthenticated when accessing tasks
- **WHEN** an unauthenticated user opens the "Minhas Tarefas" page
- **THEN** the system SHALL display a warning requesting the user to log in on the profile page

### Requirement: Filter and search academic tasks
The system SHALL allow filtering tasks by status and searching tasks by title or content.

#### Scenario: Filter tasks by status
- **WHEN** user selects a status filter option (e.g., "Pendente", "Concluída")
- **THEN** the system SHALL display only the tasks matching the chosen status

#### Scenario: Search tasks by keyword
- **WHEN** user enters a search term in the task search input
- **THEN** the system SHALL display only tasks whose title contains the search keyword

### Requirement: Update academic task status
The system SHALL allow users to update the completion status of an academic task.

#### Scenario: Mark academic task as completed
- **WHEN** user clicks the completion checkbox on an academic task card
- **THEN** the system SHALL send a PATCH request to `/academic_tasks/{id}` updating the status and refresh the interface

