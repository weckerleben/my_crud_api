# FastAPI Item Management

This project is a simple item management API built with FastAPI, SQLAlchemy, and PostgreSQL. It allows users to create, read, update, and delete items.

## Features

- RESTful API for item management
- PostgreSQL as the database
- Pydantic for data validation
- Dependency injection for services and repositories

## Requirements

- Docker and Docker Compose (recommended)
- Python 3.9+ (optional)

## Installation

### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. Set up the environment variables for PostgreSQL:
   ```bash
   export POSTGRES_USER=youruser
   export POSTGRES_PASSWORD=yourpassword
   export POSTGRES_DB=yourdbname
   ```

3. Build and run the containers:
   ```bash
   docker-compose up --build
   ```

4. Access the API at `http://localhost:8000/api/items`.

### Running with Python (Optional)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```

4. Set up the environment variables for PostgreSQL:
   ```bash
   export POSTGRES_USER=youruser
   export POSTGRES_PASSWORD=yourpassword
   export POSTGRES_DB=yourdbname
   ```

5. Run the application:
   ```bash
   uvicorn src.main:app --host 0.0.0.0 --port 8000
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
