# Spec Delta: Subjects Table

## Purpose

Defines the persistence schema for academic subjects in the database.

## ADDED Requirements

### Requirement: Subjects persistence schema
The database SHALL provide a `subjects` table linked to authenticated users.

#### Scenario: Table structure
- **WHEN** the `subjects` table is inspected
- **THEN** it contains `id` (int primary key), `user_id` (foreign key to `user`), `name` (text), `teacher` (text), `hours` (int), and `created_at` (timestamp)
- **AND** indexes exist for `id` and `user_id`
