import os
import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import settings

DATABASE_URL = settings.MYSQL_INITDB_URL


def create_db_engine():
    retries = 5
    engine = None
    while retries > 0:
        try:
            engine = create_engine(
                DATABASE_URL, connect_args={"check_same_thread": False}
            )
            print("CONNECTED TO DATABASE...")
            retries -= 1
            time.sleep(3)
        except Exception as e:
            print("DATABASE CONNECTION ERROR... " + str(e))
            retries -= 1
            time.sleep(3)
    return engine


# database engine
engine = create_db_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Provide db session to path operation functions"""
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        print("Could not connect to database... " + str(e))
    finally:
        db.close()


Base = declarative_base()

def create_tables(): 
    Base.metadata.create_all(engine)
