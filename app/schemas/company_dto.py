from pydantic import BaseModel
from uuid import UUID

class CompanyCreateDTO(BaseModel):
    name: str
    cnpj: str | None = None

    class Config:
        from_attributes = True


class CompanyUpdateDTO(BaseModel):
    name: str | None = None
    cnpj: str | None = None

class CompanyResponseDTO(BaseModel):
    id: UUID
    name: str
    cnpj: str

    class Config:
        from_attributes = True

