from sqlalchemy import Column, Integer, String
from ..database.session import Base

class Health(Base):
    __tablename__ = 'health'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    metric = Column(String, index=True)
    value = Column(Integer)
