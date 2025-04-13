# Report Generator Microservice

This repository contains a Python-based microservice built with FastAPI. The service ingests large input files, joins them with reference data, and generates reports according to configurable transformation rules. It includes scheduling (via APScheduler), JWT-based authentication, structured logging, observability, unit tests, and full containerization with Docker Compose.

## Features

- **File Upload:** Endpoints to upload `input.csv` and `reference.csv`.
- **Dynamic Report Generation:** Process files by applying transformation rules stored in an external JSON file.
- **Configuration Endpoints:** Update transformation rules dynamically using REST endpoints.
- **Scheduling:** Schedule report generation using cron expressions.
- **Security:** JWT-based authentication; endpoints are protected and require a valid token.
- **User Management:** Register new users via the `/register` endpoint.
- **Logging & Metrics:** JSON-formatted logs and a Prometheus metrics endpoint.
- **Unit Tests:** Test suite using Pytest with coverage reporting.
- **Containerization:** Docker and Docker Compose support for easy deployment along with a PostgreSQL database as a dependent service.

## Getting Started

### Prerequisites

- Python 3.10+
- Pip
- Git
- Docker (for containerized deployment)

---

## Docker Setup

1. **Build the Docker Image:**

   ```bash
   docker-compose build
   ```

2. **Run Using Docker Compose:**

   ```bash
   docker-compose up
   ```

   The service will be available at [http://localhost:8000](http://localhost:8000).

---

## Local Setup

1. **Clone the Repository:**

   ```bash
   git clone 
   cd report-generator
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the root directory with the following content:

   ```env
   DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
   JWT_SECRET_KEY=my_very_secret_key
   ```

5. **Run the Application:**

   Start the FastAPI server with Uvicorn:

   ```bash
   uvicorn app.main:app --reload
   ```

   The service will be available at [http://localhost:8000](http://localhost:8000).

6. **API Documentation:**

   - **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
   - **Redoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Project Structure

```
.
├── app
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routers
│   │   ├── auth.py
│   │   ├── health.py
│   │   ├── file_upload.py
│   │   ├── report.py
│   │   ├── config.py
│   │   └── scheduler.py
│   └── services
│       ├── file_processor.py
│       ├── report_generator.py
│       ├── transform.py
│       ├── scheduler_service.py
│       └── security.py
├── config
│   └── transform_rules.json
├── tests
│   ├── conftest.py
│   ├── test_health.py
│   ├── test_auth.py
│   └── test_report_generation.py
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .gitignore
```
---

## Running Tests

1. **Run Tests with Pytest:**

   ```bash
   pytest --maxfail=1 --disable-warnings -q
   ```

---

## Authentication and User Registration

- **Register User:**  
  Create a new user using the `/register` endpoint.
  
  **Example Request:**
  
  ```json
  {
    "username": "test",
    "password": "test123",
    "full_name": "Test User"
  }
  ```

- **Obtain Token:**  
  Use the `/token` endpoint with the registered credentials to get a JWT.
  
  **Include the token** in subsequent requests using the `Authorization` header:
  
  ```
  Authorization: Bearer <access_token>
  ```

---

## Transformation Rules

- **Rules Storage:**  
  Transformation rules are stored in `config/transform_rules.json`.
  
- **Update Rules:**  
  Use the `/config/transform-rules` endpoint to change rules. The report generation automatically applies the updated configuration.