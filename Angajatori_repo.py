from sqlalchemy.orm import Session
from fastapi import Depends, status, Response, HTTPException
from passlib.context import CryptContext
import sys

sys.path.append("/Proiect1/")
import Bazadate, Modele, schemas

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(request: schemas.User, db: Session):
    hashedpassword = pwd_cxt.hash(request.password)
    new_user = Modele.Angajatori(
        name=request.name, email=request.email, password=hashedpassword
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def arata_user(id: int, db: Session):
    user = db.query(Modele.Angajatori).filter(Modele.Angajatori.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Userul cu codul {id} nu se gaseste in baza de date",
        )
    return user
