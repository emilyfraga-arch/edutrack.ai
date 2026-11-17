# Spec Delta

## MODIFIED Requirements

### Requirement: API base URL configuration from .env
The system SHALL read the base URL for Xano authentication and CRUD endpoints primarily from Streamlit secrets (`st.secrets` / `.streamlit/secrets.toml`), while maintaining fallback compatibility with environment variables and `.env` files.

#### Scenario: Read base URL from Streamlit secrets
- **WHEN** the application executes in a Streamlit runtime with configured secrets
- **THEN** the system SHALL load the base URLs (`XANO_AUTH_BASE_URL` and `XANO_API_URL`) from `st.secrets`

#### Scenario: Read base URL from environment file
- **WHEN** the authentication module executes an API call without Streamlit secrets configured
- **THEN** the system SHALL fall back to loading the base URL from the environment or `.env` file using environment configuration
