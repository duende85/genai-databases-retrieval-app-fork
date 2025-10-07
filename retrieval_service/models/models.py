from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Airport(Base):
    __tablename__ = "airports"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    code = Column(String)

class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True)
    flight_number = Column(String)
    origin = Column(String)
    destination = Column(String)
