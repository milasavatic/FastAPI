from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Milasavaa23%40@localhost/TodoApplicationDatabase'

engine = create_engine(SQLALCHEMY_DATABASE_URI)
# , connect_args={'check_same_thread': False}) - sqlite3

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()