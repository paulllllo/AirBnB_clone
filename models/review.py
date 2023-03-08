#!/usr/bin/python3
"""A class that defines the properties of a review"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Public class attributes"""
    place_id: ""
    user_id: ""
    text: ""
