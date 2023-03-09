#!/usr/bin/python3
"""A class that defines the properties of a user"""
from models.base_model import BaseModel

class User(BaseModel):
    """Public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
