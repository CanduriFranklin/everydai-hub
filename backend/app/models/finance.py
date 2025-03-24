from sqlalchemy import Column, Integer, String, Float
from ..database.session import Base

class Finance(Base):
    __tablename__ = 'finance'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    transaction = Column(String, index=True)
    amount = Column(Float)
