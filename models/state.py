#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128),
                  nullable=False)

    cities = relationship("City",
                          backref='state',
                          cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Returns cities"""
            all_cities = self.cities
            list_cities = []
            for key, value in all_cities.items():
                if self.id == value.state_id:
                    list_cities.append(value)
            return list_cities
