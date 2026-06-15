# TodoApp FastAPI

A full-stack **FastAPI todo application** with user authentication, role-based admin panel, and interactive web interface. Demonstrates backend API development, role management, and Jinja2 template integration.

## Features

- **User Authentication** - Registration, login, logout with JWT tokens and bcrypt
- **Todo Management** - Create, read, update, delete todos; mark complete; priority levels
- **Role-Based Access** - Admin users can manage all todos and user permissions
- **Web Interface** - Jinja2 templates for login, registration, todo dashboard, and admin panel
- **Database Management** - PostgreSQL with SQLAlchemy ORM and Alembic migrations

## Tech Stack

FastAPI • PostgreSQL • SQLAlchemy • JWT • bcrypt • Jinja2 • pytest • Alembic

## Project Structure

FastAPI/ ├── TodoAPP/ │ ├── main.py # FastAPI app │ ├── database.py # DB config │ ├── models.py # SQLAlchemy models │ ├── routers/ # auth, todos, admin, users │ ├── templates/ # Jinja2 HTML pages │ ├── static/ # CSS & JavaScript │ ├── alembic/ # Database migrations │ └── tests/ # Unit tests ├── requirements.txt └── README.md

Code

## Quick Start

1. **Clone & Setup**
   ```bash
   git clone https://github.com/abenezer-gizaw/TodoApp-FastAPI.git
   cd TodoApp-FastAPI
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
Create .env

env
DATABASE_URL=postgresql://user:password@localhost/todoapp
SECRET_KEY=your-secret-key-here

Run

bash
uvicorn TodoAPP.main:app --reload
App: http://localhost:8000

Main API Endpoints

Endpoint	Method	Auth	Description
/auth/register	POST	No	Register user
/auth/login	POST	No	Login & get token
/auth/logout	POST	Yes	Logout
/todos	GET	Yes	Get user's todos
/todos	POST	Yes	Create todo
/todos/{id}	PUT	Yes	Update todo
/todos/{id}	DELETE	Yes	Delete todo
/todos/todo-page	GET	Yes	Todo dashboard (HTML)
/admin/users	GET	Yes	Get all users (admin only)
/admin	GET	Yes	Admin panel (HTML)
/users/profile	GET	Yes	Get user profile

Web Pages

Login - / - User login form
Register - /register - New user registration
Dashboard - /todos/todo-page - List & manage todos
Testing

bash
pytest                          # Run all tests
pytest -v                       # Verbose output
pytest --cov=TodoAPP tests/     # With coverage
pytest TodoAPP/tests/test_auth.py -v  # Specific test
🗄️ Database Schema

Users - id, username, email, hashed_password, is_admin, created_at
Todos - id, title, description, priority, complete, due_date, user_id (FK), created_at
Security

Passwords hashed with bcrypt
JWT token authentication
Role-based access control (Admin vs User)
Users can only access their own todos
SQL injection prevention (SQLAlchemy ORM)
Environment variables for secrets
Key Dependencies

Code
fastapi==0.135.3
sqlalchemy==2.0.49
psycopg2-binary==2.9.12
python-jose==3.5.0
bcrypt==4.0.1
jinja2==3.1.6
alembic==1.18.4
pytest==9.0.3
python-dotenv==1.2.2
Code Examples


## What I Learned

Full-stack FastAPI application
JWT authentication & session management
Role-based access control (RBAC)
Jinja2 template rendering
Database migrations with Alembic
Form handling with Starlette
Password hashing best practices
Unit testing with pytest
Admin dashboard design
Deployment

PostgreSQL database
Automatic table creation on startup
Alembic migrations for schema updates
Ready for deployment on Heroku, Railway, or similar

## Live Demo

- **API Documentation (Swagger):** https://todoapp-fastapi-4t78.onrender.com/docs
- **API Base URL:** https://todoapp-fastapi-4t78.onrender.com

Author

Abenezer Gizaw - @abenezer-gizaw