#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

# Declare the SQLAlchemy Base
Base = declarative_base() 

class BaseModel:
    """A base class for all hbnb models"""

    # Define the ID attribute as a unique primary key for the database
    id = Column(String(60), primary_key=True, nullable=False, unique=True)

    # Define created_at with a default value of the current UTC time
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Define updated_at with a default value of the current UTC time
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            from models import storage  # Import storage for saving the new instance
            self.id = str(uuid.uuid4())  # Generate a unique ID for the instance
            self.created_at = datetime.utcnow()  # Set creation time
            self.updated_at = datetime.utcnow()  # Set update time
            storage.new(self)  # Add the instance to storage
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # Parse string to datetime if the key is a timestamp
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)  # Set attributes dynamically from kwargs
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())  # Generate a new ID if not provided

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split("'")[0]  # Extract the class name
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)  # Format the string

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage  # Import storage to save the instance
        self.updated_at = datetime.utcnow()  # Update the timestamp
        storage.save()  # Persist changes to storage

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()  # Copy all attributes into a dictionary
        dictionary['__class__'] = self.__class__.__name__  # Add the class name
        dictionary['created_at'] = self.created_at.isoformat()  # Format created_at as ISO
        dictionary['updated_at'] = self.updated_at.isoformat()  # Format updated_at as ISO
        dictionary.pop('_sa_instance_state', None)  # Remove SQLAlchemy's internal state
        return dictionary

    def delete(self):
        """Deletes the current instance from storage"""
        from models import storage  # Import storage to delete the instance
        storage.delete(self)  # Remove the instance from storage
