# Report Generator Microservice

This repository contains a Python-based microservice built with FastAPI that ingests large input files and generates output reports by joining them with reference data. Transformation rules are configurable via an external JSON file and the service includes scheduling, JWT-based authentication, structured logging, and observability features.

## Features

- **File Upload:** Endpoints to upload input (`input.csv`) and reference (`reference.csv`) files.
- **Dynamic Report Generation:** Process files by applying configurable transformation rules.
- **Configuration Endpoints:** Update transformation rules dynamically via REST.
- **Scheduling:** Schedule report generation using cron expressions (via APScheduler).
- **Security:** JWT-based authentication with endpoints protected by OAuth2.
- **Structured Logging & Metrics:** JSON-formatted logs and a Prometheus metrics endpoint.
- **Unit Tests:** Tests using Pytest with coverage reporting.
- **Containerization:** Docker and Docker Compose support.

## Getting Started

### Prerequisites

- Python 3.10+
- Pip
- Git
- Docker (optional, for containerization)

### Docker Setup

1. **Build the Docker Image:**

   ```bash
   docker-compose build
   ```

2. **Run Using Docker Compose:**

   ```bash
   docker-compose up
   ```

   The service will then be accessible on [http://localhost:8000](http://localhost:8000).

### Local Setup

1. **Clone the Repository:**

   ```bash
   git clone
   cd report-generator
   ```

2. **Create a Virtual Environment and Activate It:**

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**

   Start the FastAPI server with Uvicorn:

   ```bash
   uvicorn app.main:app --reload
   ```

   The application will be available at [http://localhost:8000](http://localhost:8000).

5. **API Documentation:**

   - **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
   - **Redoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Running Tests

1. **Run Tests with Pytest:**

   ```bash
   pytest --maxfail=1 --disable-warnings -q
   ```

### Project Structure

```
.
├── app
│   ├── main.py
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
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .gitignore
```

### Authentication

- **Obtain Token:**  
  Use the `/token` endpoint with the default credentials:
  - **Username:** `test`
  - **Password:** `test123`

- **Use Token:**  
  Include the token in the `Authorization` header as:
  ```
  Authorization: Bearer <access_token>
  ```

### Transformation Rules

- The transformation rules are stored in `config/transform_rules.json`.
- Update these rules using the `/config/transform-rules` endpoint.