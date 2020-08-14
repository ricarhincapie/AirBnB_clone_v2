#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models import city, user, review
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)

    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)

    name = Column(String(128),
                  nullable=False)

    description = Column(String(1024),
                         default="",
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

    latitude = Column(Float)

    longitude = Column(Float)

    if getenv['HBNB_TYPE_STORAGE'] == db:
        reviews = relationship("Review",
                               cascade="all, delete",
                               backref="place")
    else:
        @property
        def reviews(self):
            """ """
            storage = Base.all(review.Review)
            my_list = []
            for instance in storage:
                if instance.place_id == self.id:
                    my_list.append(instance)
            return my_list
