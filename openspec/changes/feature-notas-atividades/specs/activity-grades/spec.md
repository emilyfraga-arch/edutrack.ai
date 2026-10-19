# activity-grades Specification

## Purpose
Allows professors to record and submit academic evaluation grades for students on specific academic tasks within EduTrack AI.

## ADDED Requirements

### Requirement: Professor can submit a grade for a student activity
The system SHALL allow an authenticated professor to submit an evaluation grade for a specific student on a designated academic task.

#### Scenario: Successfully submit a student grade
- **WHEN** a professor submits a valid score with student_id and academic_task_id
- **THEN** the system SHALL persist the grade record in activity_grades associated with the authenticated user_id and return confirmation

#### Scenario: Grade submission validation failure
- **WHEN** a submission is missing student_id, academic_task_id, or contains an invalid score
- **THEN** the system SHALL reject the request with a descriptive validation error

