from pydantic import BaseModel, EmailStr, SecretStr


class LinkedInCredentials(BaseModel):
    email: EmailStr
    password: SecretStr


class AppConfig(BaseModel):
    linkedin: LinkedInCredentials
