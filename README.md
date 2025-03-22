# Everydai-Hub

## Application powered by artificial intelligence

### Project Structure

```
everydai-hub/
├── backend/
│ ├── app/
│ │ ├── __init__.py
│ │ ├── main.py
│ │ ├── api/
│ │ │ ├── __init__.py
│ │ │ ├── productivity.py
│ │ │ ├── meals.py
│ │ │ ├── calendar.py
│ │ │ ├── health.py
│ │ │ ├── entertainment.py
│ │ │ ├── finance.py
│ │ │ └── digital_wellness.py
│ │ ├── models/
│ │ │ ├── __init__.py
│ │ │ ├── user.py
│ │ │ ├── task.py
│ │ │ └── meal.py
│ │ ├── services/
│ │ │ ├── __init__.py
│ │ │ ├── nebius_ai.py
│ │ │ └── auth.py
│ │ ├── database/
│ │ │ ├── __init__.py
│ │ │ └── session.py
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/
│ ├── app.py
│ ├── pages/
│ │ ├── productivity.py
│ │ ├── meals.py
│ │ ├── calendar.py
│ │ ├── health.py
│ │ ├── entertainment.py
│ │ ├── finance.py
│ │ └── digital_wellness.py
│ ├── requirements.txt
│ └── Dockerfile
├── scripts/
│ ├── setup_db.py
│ └── deploy.sh
├── docker-compose.yml
├── README.md
└── .gitignore
```

### Setup Instructions

#### Backend

1. Create a virtual environment and activate it.
2. Install the dependencies:
    ```bash
    pip install -r backend/requirements.txt
    ```
3. Run the FastAPI application:
    ```bash
    uvicorn backend.app.main:app --reload
    ```

#### Frontend

1. Create a virtual environment and activate it.
2. Install the dependencies:
    ```bash
    pip install -r frontend/requirements.txt
    ```
3. Run the Streamlit application:
    ```bash
    streamlit run frontend/app.py
    ```

#### Docker

1. Build and run the services using Docker Compose:
    ```bash
    docker-compose up --build
    ```
