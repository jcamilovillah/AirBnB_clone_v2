#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column("city_id", String(60), nullable=False,
                     ForeignKey("cities.id"))
    user_id = Column("user_id", String(60), nullable=False,
                     ForeignKey("users.id"))
    name = Column("name", String(128), nullable=True)
    description = Column("description", String(1024), nullable=True)
    number_rooms = Column("number_rooms", Interger, nullable=False, default=0)
    number_bathrooms = Column("number_bathrooms", Interger,
                              nullable=False, default=0)
    max_guest = Column("max_guset", Interger, nullable=False, default=0)
    price_by_night = Column("price_by_night", Interger,
                            nullable=False, default=0)
    latitude = Column("latitude", Float, nullable=True)
    longitude = Column("longitude", Float, nullable=True)
    amenity_ids = []
