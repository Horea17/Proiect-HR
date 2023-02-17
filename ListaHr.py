from fastapi import FastAPI
from Bazadate import engine
import Modele

from Proiect1.Routers import Angajatori, Candidati, Login

bapp = FastAPI(
    title="Aplicatie pentru angajare",
    version="0.3.0",
    description="Aplicatie de angajare unde angajatii H.R. pot sa vada diferite caracteristici ale angajatilor",
)

Modele.Base.metadata.create_all(bind=engine)
bapp.include_router(Candidati.router)
bapp.include_router(Angajatori.router)
bapp.include_router(Login.router)
