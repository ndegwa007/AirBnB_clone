#!/usr/bin/python3
"""database storage engine"""
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """interact with the MYSQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST', default='localhost')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine(
                'mysql+mysqldb://' +
                HBNB_MYSQL_USER +
                ':' +
                HBNB_MYSQL_PWD +
                '@' +
                HBNB_MYSQL_HOST +
                '/' +
                HBNB_MYSQL_DB)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current db session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current db session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes off the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from current db session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

#    def close(self):
#        """call remove() method on the private session attribute"""
#        self.__session.remove()
