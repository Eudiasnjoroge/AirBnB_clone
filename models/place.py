#!/usr/bin/python3
"""module of 'Place' class"""
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """class 'Place' that inherits from BaseModel"""
    """Represent a place.
    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids
        """

        city_id = ""
        user_id = ""
        class Place(BaseModel):
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
