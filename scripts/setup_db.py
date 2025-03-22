from app.database.session import engine
from app.models import user, task, meal

user.Base.metadata.create_all(bind=engine)
task.Base.metadata.create_all(bind=engine)
meal.Base.metadata.create_all(bind=engine)
