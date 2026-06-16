from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

Database_Url = os.getenv("DATABASE_URL")

print("DATABASE_URL =", Database_Url)
engine = create_engine(Database_Url)

session_local = sessionmaker(bind=engine,autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()