from pydantic import BaseModel, EmailStr
from user_dto import UserCreateDTO
from company_dto import CompanyCreateDTO


class RegistrationDTO(BaseModel):
    user: UserCreateDTO
    company: CompanyCreateDTO


class LoginDTO(BaseModel):
    email: EmailStr
    password: str
