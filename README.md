# FastAPI Mobile Auth Backend

A production-ready REST API backend for mobile applications built with FastAPI. Provides JWT-based authentication, user profile management, and a balance/transaction system.

## Features

- **JWT Authentication** — Access and refresh token flow for secure mobile sessions
- **User Registration & Login** — Email/password registration with bcrypt hashing
- **Profile Management** — View and update user profiles, avatar URLs
- **Balance System** — Top-up balance and transfer funds between users
- **Transaction History** — Paginated history of all user transactions
- **SQLite + SQLAlchemy** — Lightweight database with full ORM support
- **CORS Configured** — Ready for cross-origin mobile client requests
- **Auto-generated Docs** — Interactive API docs at `/docs` (Swagger UI)

## Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy 2.0
- Pydantic v2
- python-jose (JWT)
- passlib + bcrypt
- Uvicorn

## Quick Start

```bash
# Clone the repository
git clone https://github.com/qorexdev/fastapi-mobile-auth-backend.git
cd fastapi-mobile-auth-backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.
Interactive docs at `http://localhost:8000/docs`.

## Environment Variables

You can override defaults by creating a `.env` file in the project root:

| Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | (built-in default) | JWT signing key — **change in production** |
| `ALGORITHM` | `HS256` | JWT algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` | Access token lifetime |
| `REFRESH_TOKEN_EXPIRE_DAYS` | `7` | Refresh token lifetime |
| `DATABASE_URL` | `sqlite:///./app.db` | Database connection string |

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | Login and receive tokens |
| `POST` | `/auth/refresh` | Refresh access token |

### Users

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/users/me` | Get current user profile |
| `PUT` | `/users/me` | Update current user profile |
| `GET` | `/users/{user_id}` | Get user by ID |

### Balance

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/balance` | Get current balance |
| `POST` | `/balance/topup` | Top up balance |
| `POST` | `/balance/transfer` | Transfer to another user |
| `GET` | `/balance/transactions` | Get transaction history |

### Health

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |

## Project Structure

```
fastapi-mobile-auth-backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application entry point
│   ├── config.py        # Settings and configuration
│   ├── database.py      # Database engine and session
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic request/response schemas
│   ├── auth.py          # Authentication utilities
│   └── routers/
│       ├── __init__.py
│       ├── auth.py      # Auth endpoints
│       ├── users.py     # User profile endpoints
│       └── balance.py   # Balance and transaction endpoints
├── requirements.txt
├── .gitignore
└── README.md
```

## License

MIT
