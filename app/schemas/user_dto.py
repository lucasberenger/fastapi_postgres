from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserCreateDTO(BaseModel):
    name: str
    email: EmailStr
    password: str
    
    class Config:
        from_attributes = True

class UserUpdateDTO(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class UserResponseDTO(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    company: str

    class Config:
        from_attributes = True