from Proiect1.Repository import Angajatori_repo
from fastapi import APIRouter, Depends, status, HTTPException
from passlib.context import CryptContext
import sys
from sqlalchemy.orm import Session

sys.path.append("/Proiect1/")
import Bazadate, Modele, schemas

router = APIRouter(prefix="/user", tags=["Userii platformei de angajare"])


@router.post("/", response_model=schemas.ArataUser)
def create_user(request: schemas.User, db: Session = Depends(Bazadate.get_db)):
    return Angajatori_repo.create_user(request, db)


@router.get("/{id}", response_model=schemas.ArataUser)
def arata_user(id: int, db: Session = Depends(Bazadate.get_db)):
    return Angajatori_repo.arata_user(id, db)
