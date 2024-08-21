
# Data Management Platform (DMP) API

This project is a Data Management Platform (DMP) API built using FastAPI. The platform allows you to collect, organize, and activate data for advertising campaigns. The API supports first-party, second-party, and third-party data management, and provides user authentication and authorization features.

## Features

- **Data Collection**: Collect and manage first-party, second-party, and third-party data.
- **User Management**: Register and authenticate users.
- **Data Organization**: Organize data in a structured and accessible way.
- **Data Activation**: Activate data for targeted advertising campaigns.
- **API Documentation**: Interactive API documentation available via Swagger UI.



## See [FEATURES](./FEATURES.md) file for details.



## Project Structure

```
app/
├── main.py                # Entry point of the application
├── database.py            # Database configuration and session management
├── routers/               # Directory for API route handlers
│   ├── data_router.py     # Routes for data management
│   └── user_router.py     # Routes for user management
├── models/                # Directory for SQLAlchemy models
│   ├── user_models.py     # User models
│   └── data_models.py     # Data models
├── schemas/               # Directory for Pydantic schemas
│   ├── user_schemas.py    # User schemas
│   └── data_schemas.py    # Data schemas
├── static/                # Directory for static files (e.g., CSS, images)
│   ├── css/               # CSS files
│   └── images/            # Image files
└── templates/             # Directory for HTML templates
    └── index.html         # Landing page template
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/NoManNayeem/DMP.git
   cd DMP
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:

   The application uses SQLite by default. The database will be automatically created when you run the application.

5. **Run the application**:

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the application**:

   - The API will be available at `http://127.0.0.1:8000`
   - API documentation (Swagger UI) is available at `http://127.0.0.1:8000/docs`
   - The landing page is available at `http://127.0.0.1:8000/`

## Usage

- **API Documentation**: You can explore the API endpoints and test them via the Swagger UI at `http://127.0.0.1:8000/docs`.
- **User Registration**: Register new users through the `/register` endpoint.
- **Data Management**: Use the `/data` endpoints to manage first-party, second-party, and third-party data.

## Configuration

- **Database Configuration**: The application uses SQLite by default. You can modify the database configuration in `app/database.py` if you wish to use a different database engine.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

