from Bazadate import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Angajat(Base):
    __tablename__ = "Angajati"
    id = Column(Integer, primary_key=True, index=True)
    nume = Column(String)
    varsta = Column(String)
    user_id = Column(Integer, ForeignKey("Angajatori.id"))

    Angajator = relationship("Angajatori", back_populates="Angajati")


class Angajatori(Base):
    __tablename__ = "Angajatori"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    Angajati = relationship("Angajat", back_populates="Angajator")
