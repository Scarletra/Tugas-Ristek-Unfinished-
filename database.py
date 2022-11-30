from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

form = create_engine("postgresql://postgres:anjay25@localhost/<nama-database>",
    echo=True
)

Base = declarative_base()
SessionLocal = sessionmaker(bind=form)
