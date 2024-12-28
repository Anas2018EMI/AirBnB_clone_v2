#!/usr/bin/python3
"""
Defines the State class, representing states in the AirBnB clone project.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """
    Represents a state in the AirBnB clone project.
    Inherits from BaseModel and Base (SQLAlchemy).
    """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """
        Getter attribute to retrieve the list of City objects linked to this state
        when using FileStorage.
        """
        from models import storage
        from models.city import City
        return [city for city in storage.all(City).values() if city.state_id == self.id]
