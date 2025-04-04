from pydantic import BaseModel


class UserCreateDTO(BaseModel):
    name: str
    email: str
    password: str
    age: int

class UserUpdateDTO(BaseModel):
    name: str | None = None
    email: str | None = None
    age: int | None = None


class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: str
    age: int

    class Config:
        orm_mode = True