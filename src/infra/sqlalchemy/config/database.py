from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:////tmp/app_blx.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def criar_bd():
    Base.metadata.create_all(bind=engine)

def get_bd():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
