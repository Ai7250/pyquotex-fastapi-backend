from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

class TradeRequest(BaseModel):
    asset: str
    direction: str  # 'call' or 'put'
    amount: float
    duration: int = 1
