#!/usr/bin/python3
"""New engine for saving data: DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
import os


user = os.getenv("HBNB_MYSQL_USER")
passwd = os.getenv("HBNB_MYSQL_PWD")
host = os.getenv("HBNB_MYSQL_HOST")
db = os.getenv("HBNB_MYSQL_DB")
hbnb_env = os.getenv("HBNB_ENV")


class DBStorage:
    """Database mode of storage (DB engine)"""
    __engine = None
    __session = None

    def __init__(self):
        """Init method"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """
        my_dict = {}  # [class.id: {obj}
        if cls is None:
            query = self.__session.query(User, State, City,
                                         Amenity, Place, 
                                         Review).all()
            for inst in query:
                key = inst.__class__.__name__ + "." + inst.id
                my_dict[key] = inst

        else:
            query = self.__session.query(cls).all()  # A list of objects class cls

            for inst in query:
                key = inst.__class__.__name__ + "." + inst.id
                my_dict[key] = inst

        return my_dict

    def new(self, obj):
        """Adds new object to db storage"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from database"""
        Base.metadata.create_all(self.__engine)  # This brings you all the tables (classes) from DB
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session() 
