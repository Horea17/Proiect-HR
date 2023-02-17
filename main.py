from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get("/angajati")
def index(limit=10, contract: bool = True, sort: Optional[str] = None):
    if contract:
        return {"data": f"{limit} din angajatii cu contracte nedeterminate din lista"}
    else:
        return {"data": f"{limit} din toti angajatii (temporari si nedeterminati) "}


@app.get("/angajati/aplicanti")
def aplicanti():
    return {"data": "lista cu aplicanti"}


@app.get("/angajati/{nume}")
def arata(nume):
    return {"data": nume}


@app.get("/angajati/{nume}/comentarii")
def comentarii(nume):
    return {"data": {"1", "2"}}


class Angajat(BaseModel):
    nume: str
    varsta: int
    contract: Optional[bool]


@app.post("/angajati")
def adauga_angajat(angajat: Angajat):
    return {"data": f"Angajat adaugat cu numele {angajat.nume}"}
