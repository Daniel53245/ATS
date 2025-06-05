# ATS Backend

This is the backend service for the Application Tracking System (ATS), built with FastAPI and PostgreSQL.

## Project Structure

```
backend/
├── app/
│   ├── main.py           # FastAPI application entry point
│   ├── routers/          # API route handlers
│   │   └── auth.py       # Authentication routes
│   ├── models/           # Database models
│   └── schemas/          # Pydantic schemas
├── alembic/              # Database migrations
├── tests/                # Test files
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
├── start.sh            # Startup script
└── alembic.ini         # Alembic configuration
```

## Setup

### Prerequisites
- Docker and Docker Compose
- Python 3.11+ (for local development)

### Running with Docker

1. Build and start the containers:
```bash
docker-compose up --build
```

2. The backend will be available at:
- API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- OpenAPI Schema: http://localhost:8000/openapi.json

### Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

### Test Endpoint
- `GET /test-user`: Test connection to backend
  - Response: `{"msg": "Backend is connected!"}`

### Authentication Endpoints
- See `/docs` for complete API documentation

## Known Issues

### CORS and Browser Access
- When accessing the backend directly from a browser, use `http://[::1]:8000` instead of `localhost` or `127.0.0.1`
- This is due to IPv6/IPv4 resolution differences in some browsers
- The frontend application handles this automatically through the API URL configuration

### Docker Networking
- The backend service is accessible within Docker using the service name `backend:8000`
- For browser access, use `localhost:8000` or `[::1]:8000`

## Development Notes

### Database Migrations
The `start.sh` script handles database migrations automatically:
1. Waits for the database to be ready
2. Cleans old migrations
3. Generates fresh migrations
4. Applies migrations
5. Starts the FastAPI application

### Logging
- Logging is configured in `main.py`
- Request/response logging is enabled
- Log level is set to INFO

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Run tests
4. Submit a pull request

## License

MIT License 