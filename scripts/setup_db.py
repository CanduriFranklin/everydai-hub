import sys
import os

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
	from app.database.session import engine, Base
except ImportError:
	import sys
	from database.session import engine, Base

try:
	from app.models import user, task, meal
except ImportError:
	import sys
	sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app'))
	from app.models import user, task, meal

# Create all tables
Base.metadata.create_all(bind=engine)
