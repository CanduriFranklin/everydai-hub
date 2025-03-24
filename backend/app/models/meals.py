from sqlalchemy import Column, Integer, String, Table, MetaData
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = MetaData()

# Define the meals table with extend_existing=True
meals_table = Table(
    'meals', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, unique=True, nullable=False),
    Column('description', String, nullable=False),
    extend_existing=True
)

class Meals(Base):
    __tablename__ = 'meals'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
