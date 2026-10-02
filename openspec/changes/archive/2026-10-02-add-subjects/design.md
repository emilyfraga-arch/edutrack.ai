# Design

## Context

EduTrack AI currently has an initial Streamlit UI in [`app.py`](file:///c:/Users/2601914/Desktop/edutrack.ai/app.py) featuring navigation ("Dashboard", "Disciplinas", "Tarefas"), but the "Disciplinas" page and the "Disciplinas Ativas" metric are static placeholders.

The backend infrastructure utilizes Xano with XanoScript schemas in `tables/` and REST APIs in `apis/`. Per project instructions ([`AGENTS.md`](file:///c:/Users/2601914/Desktop/edutrack.ai/AGENTS.md)), XanoScript changes are orchestrated by specialized agents (Xano Table Designer and Xano API Query Writer).

## Goals / Non-Goals

**Goals:**
- Define database architecture for academic subjects (`subject` table in Xano) linked to the authenticated user.
- Define REST API contract for subject management (`apis/subjects/`) with CRUD endpoints.
- Update Streamlit UI ([`app.py`](file:///c:/Users/2601914/Desktop/edutrack.ai/app.py)) to fetch, display, and create subjects dynamically and update Dashboard metrics.

**Non-Goals:**
- Subject grade calculations and attendance tracking (reserved for subsequent changes).
- Linking tasks to subjects (reserved for the `tasks` change proposal).

## Decisions

### 1. Database Schema (`subject` table)
- **Fields**:
  - `id`: `int` (Primary Key, autoincrement)
  - `user_id`: `int` (Foreign key referencing `user.id`)
  - `name`: `text` (Required, subject name/title, trimmed)
  - `code`: `text?` (Optional, course code, e.g., "MAT101")
  - `professor`: `text?` (Optional, professor/instructor name)
  - `semester`: `text?` (Optional, e.g., "2026.1")
  - `status`: `text` (Default "active", possible values: "active", "completed", "archived")
  - `created_at`: `timestamp` (Default `now`)
- **Indexes**: Primary key on `id`, index on `user_id`, index on `status`.
- **Delegation**: Implementation assigned to **Xano Table Designer**.

### 2. REST API Group (`apis/subjects`)
- **Endpoints**:
  - `GET /subjects`: List subjects for current user (supports filter `?status=active`).
  - `POST /subjects`: Create a new subject for the authenticated user.
  - `GET /subjects/{subject_id}`: Retrieve a single subject by ID.
  - `PATCH /subjects/{subject_id}`: Update subject fields.
  - `DELETE /subjects/{subject_id}`: Remove or archive a subject.
- **Delegation**: Implementation assigned to **Xano API Query Writer**.

### 3. Frontend Architecture (`app.py`)
- Introduce an API service helper (or module) configured with `XANO_API_URL` and optional token.
- Render dynamic list of subjects in "Disciplinas" with cards/expanders showing professor, code, and status.
- Add an interactive form in "Disciplinas" to create a new subject with immediate UI refresh.
- Dynamically query active subjects count for the "Disciplinas Ativas" metric on the Dashboard.

## Risks / Trade-offs

- **[Risk]** Backend API may not be reachable if environment variables or network connectivity to Xano are missing.
  → **Mitigation**: Implement graceful error handling with informative Streamlit notification (`st.warning` / `st.error`) and mock fallback for offline local testing.
- **[Risk]** XanoScript file syntax constraints.
  → **Mitigation**: All XanoScript table schemas and query files are generated using specialized Xano agents following XanoScript syntax rules.

