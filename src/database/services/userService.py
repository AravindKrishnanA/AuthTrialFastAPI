from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from database.tables import User


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


def create_user(username: str, password_hash: str, role: str):
    user = User(username = username, password_hash = password_hash, role = role)
    session.add(user)
    session.commit()
    return {"user added": user.username}

def valid_username(username):
    username_query = session.query(User)
    valid_username_query = username_query.filter(User.username == username).with_entities(User.id)
    if not valid_username_query.first():
        return None
    return valid_username_query.first()[0]

def get_password(username):
    username_query = session.query(User)
    valid_username_query = username_query.filter(User.username == username).with_entities(User.password_hash)
    return valid_username_query.all()


def get_role(username):
    role_query = session.query(User)
    role_username_query = role_query.filter(User.username == username).with_entities(User.role)
    return str(role_username_query.all())

def add_role(username: str, role_to_add: str):
    current_role = get_role(username)
    role_query = session.query(User)
    add_role_query = role_query.filter(User.username == username)
    add_role_record = add_role_query.first()
    add_role_record.role += ", {}".format(role_to_add)

    session.commit()
    print(add_role_record.role)
    return add_role_record.role

def remove_role(username, role_to_remove):
    current_role = get_role(username)[3:-4].split(", ")
    print(current_role)
    print(role_to_remove)
    role_query = session.query(User)
    remove_role_query = role_query.filter(User.username == username)
    remove_role_record = remove_role_query.first()
    remove_role_record.role = str(current_role.remove(role_to_remove))
    session.commit()
    print(remove_role_record.role)
    return remove_role_record.role


