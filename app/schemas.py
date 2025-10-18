from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None  # Optional name

class UserCreate(UserBase):
    password: str  # Add password field

class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True