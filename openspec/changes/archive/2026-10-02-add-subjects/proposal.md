# Proposal

## Why

EduTrack AI currently lacks functionality to manage academic subjects (*disciplinas*), displaying static placeholder text in both the "Disciplinas" view and the "Dashboard" metric. Adding subject management enables students to register, view, update, and organize their enrolled subjects, establishing the essential foundation for task association, schedule management, and academic progress tracking.

## What Changes

- Introduce a new `subjects` capability covering academic subjects (disciplinas) lifecycle management.
- Define data structure requirements for subjects (name/title, course code, professor/instructor, semester/period, status, and user association).
- Define REST API requirements for managing subjects (listing active subjects, retrieving details, creating new subjects, updating, and deleting/archiving).
- Define frontend requirements in the Streamlit application (`app.py`) to display real subjects, provide interactive creation/management forms, and bind the "Disciplinas Ativas" dashboard metric.

## Capabilities

### New Capabilities
- `subjects`: Academic subject management, including data schema, backend CRUD endpoints, and frontend user interface integration.

### Modified Capabilities
<!-- None -->

## Impact

- **Database**: New table in Xano for subjects (`tables/` to be created by Xano Table Designer).
- **APIs**: New API group and endpoints in Xano (`apis/subjects/` to be created by Xano API Query Writer).
- **Frontend**: Update `app.py` to fetch and display subjects dynamically.
- **Dependencies**: HTTP client integration in Python (e.g. `requests` or `httpx`) to communicate between Streamlit and Xano APIs.

