from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#Database_Url = "postgresql+psycopg2://postgres:yaya@localhost:5432/todo_db"
Database_Url = "postgresql+psycopg2://postgres:yaya@host.docker.internal:5432/todo_db"


engine = create_engine(Database_Url)

session_local = sessionmaker(bind=engine,autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()