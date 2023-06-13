#!/usr/bin/python3
"""class state that inherits from basemodel"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """class that inherits from BaseModel"""
    if models.storage_t == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initalize and inherit"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def cities(self):
            """return a list of city instances
            where state_id equals current State.id
            """
            city_list = []
            all_cities = models.storage.all(City)

            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)

            return city_list
