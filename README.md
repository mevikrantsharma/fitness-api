# Fitness Studio Booking API

A FastAPI-based RESTful API for managing fitness studio class bookings and schedules.

## Features

- Class Management
- Booking System
- MongoDB Database Integration
- RESTful API Endpoints
- Input Validation with Pydantic
- Automated Testing with pytest

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs with Python
- **MongoDB**: NoSQL database (using Motor for async operations)
- **Pydantic**: Data validation using Python type annotations
- **Pytest**: Testing framework
- **Python-dotenv**: Environment variable management
- **Uvicorn**: ASGI server implementation

## Prerequisites

- Python 3.10+
- MongoDB
- Git

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fitness-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following variables:
```env
MONGODB_URL=your_mongodb_connection_string
DATABASE_NAME=your_database_name
```

## Project Structure

```
fitness-api/
├── routers/
│   ├── bookings.py     # Booking-related endpoints
│   └── classes.py      # Class management endpoints
├── tests/
│   ├── test_bookings.py
│   └── test_classes.py
├── database.py         # Database connection and utilities
├── main.py            # FastAPI application entry point
├── models.py          # Pydantic models
└── requirements.txt    # Project dependencies
```

## Running the Application

1. Start the server:
```bash
uvicorn main:app --reload
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

Run the tests using pytest:
```bash
pytest
```

## API Endpoints

The API provides the following endpoints:

- `GET /`: Root endpoint with welcome message
- `/classes`: Class management endpoints
- `/bookings`: Booking management endpoints

For detailed API documentation, please refer to the Swagger UI or ReDoc pages when the application is running.

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
# fitness-api
