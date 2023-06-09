from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint
from sqlalchemy.orm import declarative_base


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="postgres",
    host="localhost",
    database="ORMTest1",
    port=5432
)

engine = create_engine(url)

#creating models
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
    role = Column(String, default = "guest") #add possible check constraint

#add other tables here



Base.metadata.create_all(engine)