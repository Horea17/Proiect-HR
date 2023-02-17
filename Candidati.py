from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
import sys
from Proiect1.Repository import Candidati_repo
from sqlalchemy.orm import Session

sys.path.append("/Proiect1/")
import Bazadate, Modele, schemas


router = APIRouter(prefix="/angajati", tags=["Lista posibililor angajati"])


@router.get("/", response_model=List[schemas.Angajatraspuns])
def all(db: Session = Depends(Bazadate.get_db)):
    return Candidati_repo.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Angajat, db: Session = Depends(Bazadate.get_db)):
    return Candidati_repo.create(request, db)


@router.get("/{id}", status_code=200, response_model=schemas.Angajatraspuns)
def arata_specific(id, db: Session = Depends(Bazadate.get_db)):
    return Candidati_repo.get_specific(id, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(Bazadate.get_db)):
    return Candidati_repo.delete(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, db: Session = Depends(Bazadate.get_db)):
    return update(id, db)
