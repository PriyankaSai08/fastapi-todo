import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from main import app, Base, get_db
from dotenv import load_dotenv
import os
load_dotenv()
DATABASE_URL_TEST = os.getenv("DATABASE_URL_TEST")
engine = create_engine(DATABASE_URL_TEST)
SessionLocalTest = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = SessionLocalTest()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    test_client = TestClient(app)
    yield test_client

    Base.metadata.drop_all(bind=engine)
