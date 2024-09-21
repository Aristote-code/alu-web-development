# alu-web-development
This is for ALU frontend web development.
I will mostly include html and css as well as Javascript in this project.

# Session Authentication

This project implements session-based authentication for a simple HTTP API.

## Learning Objectives

- Understand authentication and session authentication
- Learn about Cookies: how to send and parse them
- Implement session authentication in a Flask application

## Setup

1. Install the required packages:

```
2. Set up environment variables:
   - `API_HOST`: Host for the API (default: 0.0.0.0)
   - `API_PORT`: Port for the API (default: 5000)
   - `AUTH_TYPE`: Set to 'session_auth' to enable session authentication
   - `SESSION_NAME`: Name of the session cookie

## Run the Application

```
## API Routes

- `GET /api/v1/status`: Returns the status of the API
- `GET /api/v1/stats`: Returns some stats of the API
- `GET /api/v1/users`: Returns the list of users
- `GET /api/v1/users/<id>`: Returns a user based on the ID
- `DELETE /api/v1/users/<id>`: Deletes a user based on the ID
- `POST /api/v1/users`: Creates a new user
- `PUT /api/v1/users/<id>`: Updates a user based on the ID
- `POST /api/v1/auth_session/login`: Logs in a user and creates a session
- `DELETE /api/v1/auth_session/logout`: Logs out a user and destroys the session

## Authentication

This project uses session-based authentication. When a user logs in successfully, a session is created and a session ID is stored in a cookie. Subsequent requests use this cookie for authentication.

## Files

- `api/v1/app.py`: Main application file
- `api/v1/views/index.py`: Basic API endpoints
- `api/v1/views/users.py`: User-related endpoints
- `api/v1/views/session_auth.py`: Session authentication endpoints
- `api/v1/auth/auth.py`: Base authentication class
- `api/v1/auth/basic_auth.py`: Basic authentication class
- `api/v1/auth/session_auth.py`: Session authentication class
- `models/user.py`: User model

For more details on each endpoint and authentication method, please refer to the respective files.