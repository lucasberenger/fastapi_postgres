from pydantic import BaseModel

class AuthorDTO(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class PostCreateDTO(BaseModel):
    title: str
    content: str
    author_id: int
    

class PostUpdateDTO(BaseModel):
    title: str | None = None
    content: str | None = None

class PostResponseDTO(BaseModel):
    title: str
    content: str
    author: AuthorDTO

    class Config:
        orm_mode = True