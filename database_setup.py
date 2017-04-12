import sys
from sqlalchemy import Column, ForeignKey, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250), nullable=False)

class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(80), nullable=False)
    user_id = Column(INTEGER, ForeignKey('user.id'))
    user = relationship(User)


class MenuItem(Base):
    __tablename__ = 'menu_item'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(80), nullable=False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(INTEGER, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    user_id = Column(INTEGER, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }

# to create the database file
engine = create_engine('sqlite:///restaurantmenuwithusers.db')
Base.metadata.create_all(engine)