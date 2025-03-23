# Software Structure

This document provides an overview of the project structure for the Everydai-Hub project.

## Project Structure

```plaintext
.env
.git/
.gitignore
backend/
    Dockerfile
    requirements.txt
    app/
        __init__.py
        main.py
        api/
            __init__.py
            calendar.py
            digital_wellness.py
            entertainment.py
            finance.py
            health.py
            meals.py
            productivity.py
        database/
            __init__.py
            session.py
        models/
            __init__.py
            meal.py
            task.py
            user.py
        services/
            __init__.py
            auth.py
            nebius_ai.py
custom-intructions.md
docker-compose.yml
documentation/
    end-user-guide.md
    README.md
    software-architecture.md
    software-structure.md
    technical-specifications.md
frontend/
    app.py
    Dockerfile
    requirements.txt
    pages/
        calendar.py
        digital_wellness.py
        entertainment.py
        finance.py
        health.py
        meals.py
        productivity.py
main.py
README.md
scripts/
    deploy.sh
    setup_db.py
venv/
```

## Description of Key Directories and Files

- **backend/**: Contains the backend code for the project.
  - **Dockerfile**: Docker configuration for the backend.
  - **requirements.txt**: Python dependencies for the backend.
  - **app/**: Main application code.
    - **api/**: API endpoints for different functionalities.
    - **database/**: Database configuration and session management.
    - **models/**: Database models.
    - **services/**: Service layer for business logic.
- **custom-intructions.md**: Custom instructions for the project.
- **docker-compose.yml**: Docker Compose configuration.
- **documentation/**: Project documentation.
- **frontend/**: Contains the frontend code for the project.
  - **Dockerfile**: Docker configuration for the frontend.
  - **requirements.txt**: Python dependencies for the frontend.
  - **pages/**: Frontend pages for different functionalities.
- **main.py**: Entry point for the application.
- **README.md**: Project README file.
- **scripts/**: Utility scripts for deployment and setup.
- **venv/**: Virtual environment for the project.

This structure ensures a clear separation of concerns and modularity, making the project easier to maintain and extend.
