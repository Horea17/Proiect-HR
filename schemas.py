from typing import Optional, List
from pydantic import BaseModel


class Angajatmodel(BaseModel):
    nume: str
    varsta: int
    contract: Optional[bool]


class Angajat(Angajatmodel):
    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ArataUser(BaseModel):
    name: str
    email: str
    Angajati: List[Angajat] = []

    class Config:
        orm_mode = True


class Angajatraspuns(BaseModel):
    nume: str
    varsta: int
    Angajator: ArataUser

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str
