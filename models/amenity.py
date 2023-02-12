#!/usr/bin/python3
"""Amenity class defined."""
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.
    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
