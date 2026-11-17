# auth-profile Specification

## Purpose
Provides user authentication and profile management in the Streamlit application by integrating with Xano auth endpoints (`auth/signup`, `auth/login`, `auth/me`) and configuring the base URL via an environment file.

## Requirements

### Requirement: User registration via auth/signup
The system SHALL allow a new user to register an account by providing their name, email, and password, sending the data to the Xano `auth/signup` endpoint and storing the user in the `user` table.

#### Scenario: Successful user registration
- **WHEN** a user fills in valid name, email, and password and submits the registration form
- **THEN** the system SHALL send a POST request to `auth/signup`, receive the authentication token, store it in `st.session_state`, and display a success message

#### Scenario: Registration failure with duplicate email
- **WHEN** a user attempts to sign up with an email that is already in use
- **THEN** the system SHALL display an error message alerting that the account is already registered

### Requirement: User authentication via auth/login
The system SHALL allow an existing user to log in with their email and password through the Xano `auth/login` endpoint.

#### Scenario: Successful login
- **WHEN** a user provides valid email and password credentials and submits the login form
- **THEN** the system SHALL send a POST request to `auth/login`, save the returned auth token and user_id in `st.session_state`, and load the user profile

#### Scenario: Failed login with invalid credentials
- **WHEN** a user provides invalid email or password credentials
- **THEN** the system SHALL display an authentication error message and keep the user in the unauthenticated state

### Requirement: User profile retrieval and logout via auth/me
The system SHALL retrieve authenticated user data using the `auth/me` endpoint with the stored Bearer token, and allow the user to terminate their session.

#### Scenario: View authenticated user profile
- **WHEN** an authenticated user accesses `pages/3_👤_Perfil.py`
- **THEN** the system SHALL send a GET request to `auth/me` with the Bearer token in the Authorization header and display user details (name, email, role, id)

#### Scenario: User logout
- **WHEN** an authenticated user clicks the logout button
- **THEN** the system SHALL clear the authentication token and user data from `st.session_state` and display the login/signup interface

### Requirement: API base URL configuration from .env
The system SHALL read the base URL for Xano authentication and CRUD endpoints primarily from Streamlit secrets (`st.secrets` / `.streamlit/secrets.toml`), while maintaining fallback compatibility with environment variables and `.env` files.

#### Scenario: Read base URL from Streamlit secrets
- **WHEN** the application executes in a Streamlit runtime with configured secrets
- **THEN** the system SHALL load the base URLs (`XANO_AUTH_BASE_URL` and `XANO_API_URL`) from `st.secrets`

#### Scenario: Read base URL from environment file
- **WHEN** the authentication module executes an API call without Streamlit secrets configured
- **THEN** the system SHALL fall back to loading the base URL from the environment or `.env` file using environment configuration
