from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = "sqlite:///./blog_database.py"

engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})
sessionLocal= sessionmaker(autoflush= False, autocommit= False, bind= engine)
Base = declarative_base()

def get_db():
    db= sessionLocal()
    try:
        yield db
    finally:
        db.close()
