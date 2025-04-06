# PyQuotex FastAPI Backend

A backend server using FastAPI and PyQuotex to connect to Quotex and handle trading signals.

## 🔧 Features

- Login to Quotex account
- Fetch account balance
- Place a trade (call/put)

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/pyquotex-fastapi-backend.git
cd pyquotex-fastapi-backend

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```

## 📬 API Endpoints

| Method | Endpoint    | Description         |
|--------|-------------|---------------------|
| POST   | /login      | Login to Quotex     |
| GET    | /balance    | Get account balance |
| POST   | /trade      | Place a trade       |

## ⚠️ Warning

Use only on demo accounts. This is an unofficial API.
