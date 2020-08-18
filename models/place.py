#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship, backref
from models.review import Review
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(60),
                  nullable=False)
    description = Column(String(1024),
                         nullable=True)
    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)
    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)
    max_guest = Column(Integer,
                       nullable=False,
                       default=0)
    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)
    latitude = Column(Float,
                      nullable=True)
    longitude = Column(Float,
                       nullable=True)

    amenities_ids = []

    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """getter amenity that returns the list of Amenity"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            "Setter amenities"
            if "Amenity" == type(obj).__name__:
                self.amenities_ids.append(obj.id)


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=True))
