# Spec Delta

## Purpose

Provides automated calculation of academic subject progress based on completed versus total tasks fetched from Xano CRUD endpoints, returning structured JSON results.

## ADDED Requirements

### Requirement: Subject progress calculation based on tasks
The system SHALL compute the progress of a given subject by fetching its academic tasks through the CRUD endpoints and calculating the percentage of completed tasks relative to total tasks.

#### Scenario: Successfully calculate progress with mixed tasks
- **WHEN** user requests progress calculation for a subject having 4 total tasks (3 completed and 1 pending)
- **THEN** system returns a JSON payload indicating 4 total tasks, 3 completed tasks, 1 pending task, and a progress percentage of 75.0%

#### Scenario: Calculate progress when all tasks are completed
- **WHEN** user requests progress calculation for a subject where all tasks are completed
- **THEN** system returns a JSON payload with progress percentage equal to 100.0%

### Requirement: Handle subjects without tasks
The system SHALL handle subjects that have no registered tasks without encountering division by zero errors, setting the progress percentage to 0.0%.

#### Scenario: Subject with zero tasks
- **WHEN** user requests progress calculation for a subject that has no registered academic tasks
- **THEN** system returns a JSON payload with total_tasks equal to 0, completed_tasks equal to 0, pending_tasks equal to 0, and progress_percentage equal to 0.0%

### Requirement: Structured JSON response payload
The system SHALL return the calculated progress encapsulated in a well-defined JSON object containing subject identification, task counters, and percentage.

#### Scenario: Valid JSON output structure
- **WHEN** progress calculation completes successfully
- **THEN** system outputs a JSON object containing the keys "subject_id", "subject_name", "total_tasks", "completed_tasks", "pending_tasks", and "progress_percentage"

### Requirement: Error handling for missing subject or invalid authentication
The system SHALL properly handle situations where the subject does not exist, network fails, or authentication is missing or invalid.

#### Scenario: Subject not found or access denied
- **WHEN** progress calculation is requested for a non-existent subject ID or without valid credentials
- **THEN** system returns a JSON object containing an "error" key explaining the failure reason

