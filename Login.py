import sys

sys.path.append("/Proiect1/")
import Bazadate, Modele, schemas
from passlib.context import CryptContext
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import hashlib

router = APIRouter(tags=["Authentification"])


@router.post("/login")
def login(request: schemas.Login, db: Session = Depends(Bazadate.get_db)):
    user = (
        db.query(Modele.Angajatori)
        .filter(Modele.Angajatori.name == request.username)
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Username"
        )
    if not (user.password == request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Password"
        )
    return user
