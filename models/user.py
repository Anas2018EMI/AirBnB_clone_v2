#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'

    # Define email as a required string column
    email = Column(String(128), nullable=False)

    # Define password as a required string column
    password = Column(String(128), nullable=False)

    # Define first_name as an optional string column
    first_name = Column(String(128), nullable=True)

    # Define last_name as an optional string column
    last_name = Column(String(128), nullable=True)
