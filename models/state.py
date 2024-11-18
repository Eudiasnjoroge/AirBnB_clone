#!/usr/bin/python3
"""module of 'State' class"""
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """class 'State' that inherits from BaseModel"""
    """Represent a state.
    name = ""
    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
    name = ""
