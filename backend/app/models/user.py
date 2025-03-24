from sqlalchemy import Column, Integer, String, Table, MetaData
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = MetaData()

# Define the users table with extend_existing=True
users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, unique=True, nullable=False),
    Column('email', String, unique=True, nullable=False),
    Column('password', String, nullable=False),
    extend_existing=True
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
