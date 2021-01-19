#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if os.getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self):
            """return the list of City objects"""
            _cities = []
            for _id, city in models.storage.all(City).items():
                if self.id == city.state_id:
                    _cities.append(city)
            return _cities

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete")
