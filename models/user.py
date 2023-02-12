#!/usr/bin/python3
"""Defines the User class."""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """Represents the User of the platform.
    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email of the user.
        password (str): The password of the user."""
        
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
