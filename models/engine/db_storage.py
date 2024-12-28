#!/usr/bin/python3

"""
Implements the DBStorage engine for data persistence using MySQL and SQLAlchemy.
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """
    Interacts with the MySQL database using SQLAlchemy.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize the DBStorage engine.
        """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{database}",
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all objects or all objects of a specific class.
        """
        objects = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        else:
            for subclass in [User, State, City, Amenity, Place, Review]:
                for obj in self.__session.query(subclass).all():
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj
        return objects

    def new(self, obj):
        """
        Add the object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes to the database.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete the object from the current database session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload all tables in the database and create a new session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """
        Close the current session.
        """
        self.__session.close()
