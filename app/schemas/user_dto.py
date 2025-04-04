from pydantic import BaseModel


class UserCreateDTO(BaseModel):
    name: str
    email: str
    password: str
    age: int


class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: str
    age: int

    class Config:
        orm_mode = True