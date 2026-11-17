# Spec Delta

## Purpose

Enables generation and downloading of student academic performance reports in PDF format through an automated Python script and an authenticated Xano backend endpoint.

## ADDED Requirements

### Requirement: Student performance PDF generation
The system SHALL provide an automated script to generate a formatted PDF document detailing the student's academic performance, including student profile information, registered subjects, academic tasks with completion status, and overall progress metrics.

#### Scenario: Generate PDF report for student with active subjects and tasks
- **WHEN** the script is executed for an authenticated student with registered subjects and tasks
- **THEN** system generates a PDF document containing student identification, subject summaries, task completion status, and overall progress percentage

#### Scenario: Generate PDF report for student with no registered tasks
- **WHEN** the script is executed for a student who has subjects but no academic tasks
- **THEN** system generates a PDF document displaying the enrolled subjects and indicating 0 total tasks and 0.0% completion rate

### Requirement: Download student report endpoint in Xano
The backend system SHALL expose an authenticated endpoint in Xano (`GET /reports/student_performance_pdf`) that verifies JWT credentials, aggregates the student's performance data or provides the downloadable report file, and restricts data to the authenticated user ($auth.id).

#### Scenario: Authenticated student downloads report
- **WHEN** an authenticated user calls the report endpoint with a valid Bearer token
- **THEN** system returns the student performance report data or downloadable payload associated strictly with the user's account

#### Scenario: Unauthenticated request rejected
- **WHEN** a client calls the report endpoint without a valid authentication token
- **THEN** system SHALL reject the request with HTTP 401 Unauthorized

### Requirement: Security and multitenant isolation for report generation
The system SHALL enforce that report generation and download queries strictly filter records where user_id matches the authenticated user ($auth.id), preventing unauthorized access to other students' academic data.

#### Scenario: User queries report
- **WHEN** a user generates or requests their performance report
- **THEN** the report includes only records where user_id equals $auth.id
