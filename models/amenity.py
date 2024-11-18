#!/usr/bin/python3
"""module of 'Amenity' class"""
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class 'Amenity' that inherits from BaseModel"""
    """Represent an amenity.

    name = ""
    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
    name = ""
