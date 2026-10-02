# Tasks

## 1. Database Model (Xano Backend)

- [x] 1.1 Design and create the `subject` table schema file in `tables/` with fields (`id`, `user_id`, `name`, `code`, `professor`, `semester`, `status`, `created_at`) via Xano Table Designer and verify schema syntax.
- [x] 1.2 Configure indexes for `id` (primary), `user_id`, and `status` in the table definition and verify file format.

## 2. API Endpoints (Xano Backend)

- [x] 2.1 Create API group `apis/subjects/` and implement `GET /subjects` query to list user subjects (with status filter) via Xano API Query Writer.
- [x] 2.2 Implement `POST /subjects` query in `apis/subjects/` to validate input and insert a new subject record via Xano API Query Writer.
- [x] 2.3 Implement `GET /subjects/{subject_id}` query in `apis/subjects/` to retrieve single subject details via Xano API Query Writer.
- [x] 2.4 Implement `PATCH /subjects/{subject_id}` query in `apis/subjects/` to update subject properties via Xano API Query Writer.
- [x] 2.5 Implement `DELETE /subjects/{subject_id}` query in `apis/subjects/` to remove or archive a subject record via Xano API Query Writer.

## 3. Frontend Integration (Streamlit `app.py`)

- [x] 3.1 Implement a Python API client service to handle requests to Xano subject endpoints with environment variable configuration and graceful fallback.
- [x] 3.2 Update the "Disciplinas" view in `app.py` to render the subjects list and provide an interactive form for creating new subjects.
- [x] 3.3 Update the "Dashboard" view in `app.py` to compute and display the active subjects count in the "Disciplinas Ativas" metric.
- [x] 3.4 Test the Streamlit application flow locally to verify subject creation, list rendering, and metric updates.

