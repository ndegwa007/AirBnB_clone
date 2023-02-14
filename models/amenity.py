#!/usr/bin/env python3
"""class that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """contains public class attribute name"""
    name = ""
