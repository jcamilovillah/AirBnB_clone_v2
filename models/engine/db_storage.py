#!/usr/bin/python3
""" DBStorage Module for HBNB project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:

    """ Engine """
    __engine = None
    __session = None

    def __init__(self):
        """init method"""
        user = getenv("HBNB_MYSQL_USER")
        passw = getenv("HBNB_MYSQL_PWD")
        lc = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user, passw, lc, db),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        objs = {}
        if cls is None:
            consulta = self.__session.query(User, State, City, Amenity,
                                            Place, Review)
            for obj in consulta:
                name_cl = type(obj).__name__ + "." + str(obj.id)
                objs[name_cl] = obj
        else:
            consulta1 = self.__session.query(cls).all()
            for obj in consulta1:
                name_cl = type(obj).__name__ + "." + str(obj.id)
                objs[name_cl] = obj
        return objs

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit changes in db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and
        create the current database session"""
        Base.metadata.create_all(self.__engine)
        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_factory)
        self.__session = Session()

    def close(self):
        """ call remove() method on the private session attribute"""
        self.__session.close()
