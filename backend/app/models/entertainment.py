from sqlalchemy import Column, Integer, String
from ..database.session import Base

class Entertainment(Base):
    __tablename__ = 'entertainment'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    content = Column(String, index=True)
    duration = Column(Integer)
