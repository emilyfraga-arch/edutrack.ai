# Design: Create Subjects Table

## Context

Per [`AGENTS.md`](file:///c:/Users/2601914/Desktop/edutrack.ai/AGENTS.md), schema changes in EduTrack AI are designed in XanoScript within the `tables/` directory using specialized agents. Authentication in this workspace is handled by the `user` table (`tables/752251_user.xs` with `auth = true`).

## Database Schema (`subjects` table)

- **Table Name**: `subjects`
- **Auth**: `false`
- **Schema Fields**:
  - `id`: `int` (Primary key, auto-increment)
  - `user_id`: `int` (Foreign key referencing `user` table)
  - `name`: `text filters=trim` (Required subject name)
  - `teacher`: `text? filters=trim` (Optional instructor/professor name)
  - `hours`: `int?` (Optional workload hours)
  - `created_at`: `timestamp?=now` (Record creation timestamp)
- **Indexes**:
  - Primary key on `id`
  - B-tree index on `user_id` (asc)
