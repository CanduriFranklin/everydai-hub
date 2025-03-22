import sys
import os

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database.session import engine, Base
from app.models import user, task, meal

# Create all tables
Base.metadata.create_all(bind=engine)
