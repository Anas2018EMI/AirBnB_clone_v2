#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    # Define the name of the city as a required string column
    name = Column(String(128), nullable=False)

    # Define the state_id as a foreign key linking to the states table
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
