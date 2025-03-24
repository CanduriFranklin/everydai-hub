import datetime
from sqlalchemy import Column, Integer, String, DateTime
from .database.session import Base, SessionLocal

class AppBehavior(Base):
    __tablename__ = 'app_behavior'

    id = Column(Integer, primary_key=True)
    event = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, event):
        self.event = event

def log_event(event):
    session = SessionLocal()
    app_behavior = AppBehavior(event=event)
    session.add(app_behavior)
    session.commit()
    session.close()