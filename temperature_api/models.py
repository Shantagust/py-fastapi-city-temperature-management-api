from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

from city_api.models import City
from database import Base


class Temperature(Base):
    __tablename__ = 'temperature'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('city.id'))
    date_time = Column(Date)
    temperature = Column(Integer)
    city = relationship(City)
