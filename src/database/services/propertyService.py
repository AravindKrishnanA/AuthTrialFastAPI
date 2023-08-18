from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from database.tables import Property


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="postgres",
    host="localhost",
    database="ORMTest1",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()


def create_property(owner_id: int, name: str, type: str, nunits: int, floors: int):
    property = Property(owner_id = owner_id, name = name, type = type, nunits = nunits, floors = floors)
    session.add(property)
    session.commit()
    return {"property added" : property.name}

def get_all_property(name: str):
    property_query = session.query(Property)
    property_details_query = property_query.filter(Property.name == name)
    return property_details_query.all()

def get_owned_properties(owner_id: int):
    property_query = session.query(Property)
    property_owned_details_query = property_query.filter(Property.owner_id == owner_id)
    print(property_owned_details_query.all())
    return property_owned_details_query.all()

