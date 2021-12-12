from typing import Optional
from pydantic import BaseModel, SecretStr
from pydantic.networks import EmailStr

class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    password: str
