#!/usr/bin/python3
"""City class defined."""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new City.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(**kwargs)
