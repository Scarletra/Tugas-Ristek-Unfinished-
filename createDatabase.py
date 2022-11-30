from database import Base, form
from models import Item

print("Creating database .....")


Base.metadata.create_all(form)