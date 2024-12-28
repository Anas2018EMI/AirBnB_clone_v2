#!/usr/bin/python3
"""
Defines the Review class, representing reviews in the AirBnB clone project.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """
    Represents a review in the AirBnB clone project.
    Inherits from BaseModel and Base (SQLAlchemy).
    """

    __tablename__ = 'reviews'

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
