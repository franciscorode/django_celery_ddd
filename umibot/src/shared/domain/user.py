from uuid import UUID

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    public_id: UUID
    name: str
    email: EmailStr
    phone_number: str
    origin: str
