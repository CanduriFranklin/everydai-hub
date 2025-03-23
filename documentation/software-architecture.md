# Software Architecture

This document provides a detailed description of the software architecture for the Everydai-Hub project.

## Overview

Everydai-Hub is an AI-powered application that provides various functionalities such as productivity assistance, meal planning, smart calendar, health tracking, entertainment recommendations, financial management, and digital wellness. The architecture is designed to ensure seamless integration between the backend and frontend, leveraging AI capabilities for enhanced user experience.

## Components

### Backend

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **SQLAlchemy**: An SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Nebius AI SDK**: A software development kit for integrating Nebius AI Studio.

### Frontend

- **Streamlit**: An open-source app framework for Machine Learning and Data Science teams.

### Database

- **PostgreSQL**: An open-source relational database management system.

### Monitoring

- **Prometheus**: An open-source systems monitoring and alerting toolkit.
- **Grafana**: An open-source platform for monitoring and observability.

## Flowchart

Below is a flowchart that visualizes the software architecture and the interaction between different components.

![Software Architecture Diagram](../images/software-architecture-diagram.png)

```mermaid
graph TD;
    A[User] -->|Interacts with| B[Frontend (Streamlit)];
    B -->|Sends requests to| C[Backend (FastAPI)];
    C -->|Fetches data from| D[Database (PostgreSQL)];
    C -->|Integrates with| E[Nebius AI SDK];
    C -->|Sends metrics to| F[Prometheus];
    F -->|Displays metrics on| G[Grafana];
```

## Detailed Description

### User Interaction

1. **Frontend (Streamlit)**: Users interact with the application through the Streamlit frontend. Each page corresponds to a specific functionality (e.g., productivity, meals, calendar, etc.).

2. **Backend (FastAPI)**: The frontend sends requests to the FastAPI backend, which handles the business logic and processes the requests.

### Data Management

1. **Database (PostgreSQL)**: The backend interacts with the PostgreSQL database to store and retrieve data. SQLAlchemy is used as the ORM to define and manage the database models.

### AI Integration

1. **Nebius AI SDK**: The backend integrates with Nebius AI Studio using the Nebius AI SDK to perform AI-powered inferences. The results are then sent back to the frontend for display.

### Performance Monitoring

1. **Prometheus**: The backend sends metrics to Prometheus for monitoring the performance and health of the application.

2. **Grafana**: Grafana is used to visualize the metrics collected by Prometheus, providing insights into the application's performance.

## Conclusion

The software architecture of Everydai-Hub is designed to ensure a seamless and efficient user experience by integrating various components and leveraging AI capabilities. The flowchart provides a visual representation of the interaction between different components, highlighting the data flow and integration points.
