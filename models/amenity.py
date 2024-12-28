#!/usr/bin/python3
"""
Defines the Amenity class, representing amenities in the AirBnB clone project.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """
    Represents an amenity in the AirBnB clone project.
    Inherits from BaseModel and Base (SQLAlchemy).
    """

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place", secondary="place_amenity", back_populates="amenities")
