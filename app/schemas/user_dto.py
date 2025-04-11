from pydantic import BaseModel, EmailStr


class UserCreateDTO(BaseModel):
    name: str
    email: EmailStr
    password_hash: str
    
    class Config:
        from_attributes = True

class UserUpdateDTO(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int

    class Config:
        from_attributes = True