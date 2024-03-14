# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_USER, DB_HOST, DB_NAME, DB_PASS, DB_PORT

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:djtynjhu@localhost:5432/postgres"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()
