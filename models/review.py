#!/usr/bin/python3
"""module of 'Review' class"""
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """class 'Review' that inherits from BaseModel"""
    """Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
