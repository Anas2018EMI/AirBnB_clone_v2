#!/usr/bin/python3
"""
This module initializes the storage system for the HBNB project.
"""
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')  # Determine the storage type from environment variables

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()  # Initialize DBStorage if storage type is 'db'
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()  # Default to FileStorage

storage.reload()  # Reload objects from storage
