#!/usr/bin/python3
"""Module used to define a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review


class User(BaseModel, Base):
    """Class user with it's attributes"""
