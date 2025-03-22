# Software Structure

This document outlines the software structure of the Everydai-Hub project.

## Backend

The backend is built using FastAPI and includes the following components:

- **API Endpoints**: Defined in the `api` directory.
- **Database Models**: Defined in the `models` directory.
- **Services**: Business logic and integrations in the `services` directory.
- **Database Configuration**: Set up in the `database` directory.

## Frontend

The frontend is built using Streamlit and includes the following components:

- **Main Application**: Entry point in `app.py`.
- **Pages**: Individual pages for each functionality in the `pages` directory.

## Database

The database is configured using SQLAlchemy and PostgreSQL. Models are defined for users, tasks, and meals.

## AI Integration

Nebius AI Studio is integrated to provide AI-powered features. The integration logic is implemented in the `services/nebius_ai.py` file.

## Deployment

The application is containerized using Docker. Docker Compose is used to manage the services, including the backend, frontend, and database.

## Monitoring

Prometheus and Grafana are used to monitor the performance and health of the application.
