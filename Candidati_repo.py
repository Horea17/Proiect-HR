from sqlalchemy.orm import Session
from fastapi import Depends, status, Response, HTTPException
import sys

sys.path.append("/Proiect1/")
import Bazadate, Modele, schemas


def get_all(db: Session):
    angajati = db.query(Modele.Angajat).all()
    return angajati


def create(request: schemas.Angajat, db: Session):
    angajat_nou = Modele.Angajat(nume=request.nume, varsta=request.varsta, user_id=1)
    db.add(angajat_nou)
    db.commit()
    db.refresh(angajat_nou)
    return angajat_nou


def delete(id: int, db: Session = Depends(Bazadate.get_db)):
    angajat = db.query(Modele.Angajat).filter(Modele.Angajat.id == id)
    if not angajat.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Angajatul cu codul {id} nu se gaseste in baza de date",
        )
    else:
        angajat.delete(synchronize_session=False)
    db.commit()
    return {"rezolvat"}


def update(id: int, request: schemas.Angajat, db: Session = Depends(Bazadate.get_db)):
    angajat = db.query(Modele.Angajat).filter(Modele.Angajat.id == id)
    if not angajat.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Angajatul cu codul {id} nu se gaseste in baza de date",
        )
    else:
        angajat.update({"nume": request.nume, "varsta": request.varsta})
    db.commit()
    return {"modificat"}


def get_specific(
    id: int, request: schemas.Angajat, db: Session = Depends(Bazadate.get_db)
):
    angajat = db.query(Modele.Angajat).filter(Modele.Angajat.id == id).first()
    if not angajat:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Angajatul cu codul {id} nu se gaseste in baza de date",
        )
        """response.status_code = status.HTTP_404_NOT_FOUND
        return {"Comentariu": f"Angajatul cu codul {id} nu se gaseste in baza de date"}"""
    return angajat
