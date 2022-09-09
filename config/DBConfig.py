import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()
engine = db.create_engine("sqlite:///PyFlora.db", echo=False)