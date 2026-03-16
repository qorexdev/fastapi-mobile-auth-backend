<p align="center">
  <h1 align="center">FastAPI Mobile Auth Backend</h1>
  <p align="center">Production-ready REST API backend for mobile applications with JWT authentication, user management, and a balance/transaction system.</p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.104-009688?style=flat&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Pydantic-v2-E92063?style=flat&logo=pydantic&logoColor=white" alt="Pydantic">
  <img src="https://img.shields.io/badge/JWT-Auth-000000?style=flat&logo=jsonwebtokens&logoColor=white" alt="JWT">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat" alt="License">
</p>

---

## Features

- **JWT Authentication** — access and refresh token flow for secure mobile sessions
- **User Registration & Login** — email/password registration with bcrypt hashing
- **Profile Management** — view and update user profiles, avatar URLs
- **Balance System** — top-up balance and transfer funds between users
- **Transaction History** — paginated history of all user transactions
- **SQLite + SQLAlchemy** — lightweight database with full ORM support
- **CORS Configured** — ready for cross-origin mobile client requests
- **Auto-generated Docs** — interactive Swagger UI at `/docs`

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

Override defaults by creating a `.env` file in the project root:

| Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | built-in default | JWT signing key — **change in production** |
| `ALGORITHM` | `HS256` | JWT algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` | Access token lifetime |
| `REFRESH_TOKEN_EXPIRE_DAYS` | `7` | Refresh token lifetime |
| `DATABASE_URL` | `sqlite:///./app.db` | Database connection string |

## API Documentation

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

### Balance & Transactions

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/balance` | Get current balance |
| `POST` | `/balance/topup` | Top up balance |
| `POST` | `/balance/transfer` | Transfer to another user |
| `GET` | `/balance/transactions` | Get transaction history (paginated) |

### Health

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |

## Project Structure

```
fastapi-mobile-auth-backend/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI application entry point
│   ├── config.py           # Settings and configuration
│   ├── database.py         # Database engine and session
│   ├── models.py           # SQLAlchemy models (User, Transaction)
│   ├── schemas.py          # Pydantic request/response schemas
│   ├── auth.py             # JWT token utilities
│   └── routers/
│       ├── __init__.py
│       ├── auth.py         # Auth endpoints
│       ├── users.py        # User profile endpoints
│       └── balance.py      # Balance and transaction endpoints
├── requirements.txt
├── .gitignore
└── README.md
```

## Tech Stack

| Component | Technology |
|---|---|
| Framework | FastAPI 0.104 |
| ORM | SQLAlchemy 2.0 |
| Validation | Pydantic v2 |
| Auth | python-jose (JWT) + passlib/bcrypt |
| Server | Uvicorn |
| Database | SQLite (swappable via `DATABASE_URL`) |

## License

MIT

---

<p align="center">
  <sub>developed by <a href="https://github.com/qorexdev">qorex</a></sub>
  <br>
  <sub>
    <a href="https://github.com/qorexdev">GitHub</a> · <a href="https://t.me/qorexdev">Telegram</a>
  </sub>
</p>
