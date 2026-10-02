# Proposal: Create Subjects Table

## Why

EduTrack AI needs persistence for academic subjects (*disciplinas*) associated with authenticated users in the Xano backend. Defining the `subjects` table schema enables storing subject metadata including subject title, instructor, total workload hours, and user ownership.

## What Changes

- Create the `subjects` table schema in XanoScript (`tables/subjects.xs`).
- Associate each subject with an authenticated user via a foreign key reference to `user`.
- Define table indexes for primary key identification and efficient query filtering by `user_id`.

## Capabilities

### New Capabilities
- `subjects-table`: Database schema model for academic subjects in Xano.

### Modified Capabilities
<!-- None -->

## Impact

- **Database**: Adds `tables/subjects.xs` schema file conforming to XanoScript standards.
