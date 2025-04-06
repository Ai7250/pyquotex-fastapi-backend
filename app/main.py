from fastapi import FastAPI, HTTPException
from app.quotex_api import QuotexClient
from app.models import LoginRequest, TradeRequest

app = FastAPI()
client = None

@app.post("/login")
def login(data: LoginRequest):
    global client
    client = QuotexClient(data.email, data.password)
    if client.connect():
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Login failed")

@app.get("/balance")
def get_balance():
    if client:
        balance = client.get_profile()
        if balance:
            return {"balance": balance}
    raise HTTPException(status_code=403, detail="Not connected")

@app.post("/trade")
def place_trade(trade: TradeRequest):
    if client:
        result = client.place_trade(trade.asset, trade.direction, trade.amount, trade.duration)
        if result:
            return {"message": "Trade placed", "result": result}
    raise HTTPException(status_code=400, detail="Trade failed or not logged in")
