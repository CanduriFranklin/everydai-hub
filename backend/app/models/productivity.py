from sqlalchemy import Column, Integer, String
from ..database.session import Base

class Productivity(Base):
    __tablename__ = 'productivity'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    task = Column(String, index=True)
    duration = Column(Integer)
