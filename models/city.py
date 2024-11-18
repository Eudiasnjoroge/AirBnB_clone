#!/usr/bin/python3
"""module of 'City' class"""
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """class 'City' that inherits from BaseModel"""
    """Represent a city.
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
