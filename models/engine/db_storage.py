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

