from sqlalchemy import Column, Integer, String
from ..database.session import Base

class DigitalWellness(Base):
    __tablename__ = 'digital_wellness'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    activity = Column(String, index=True)
    duration = Column(Integer)
