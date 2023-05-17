from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean
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
Session = sessionmaker(bind=engine)
session = Session()


#creating models
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_done = Column(Boolean, default=False)



Base.metadata.create_all(engine)

def create_todo(text: str, is_complete: bool = False):
    todo = Todo(text=text, is_done=is_complete)
    session.add(todo)
    session.commit()
    return {"todo added": todo.text}

create_todo(text="first todo", is_complete=True)
create_todo(text="second todo", is_complete=True)
create_todo(text="third todo", is_complete=True)