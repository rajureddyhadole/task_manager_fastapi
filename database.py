from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# 1. Define the SQLite database URL
# For SQLite, the URL starts with 'sqlite:///'.
# './test.db' creates a file named test.db in your local directory.
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# 2. Create the SQLAlchemy engine
# 'connect_args={"check_same_thread": False}' is REQUIRED only for SQLite.
# It allows FastAPI to interact with the database across multiple threads safely.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Create a configured "Session" class
# In SQLAlchemy 2.0, autoflush=False and expire_on_commit=False remain standard practices.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 4. Create the SQLAlchemy 2.0 Declarative Base class
# This replaces the older `declarative_base()` function from SQLAlchemy 1.x.
class Base(DeclarativeBase):
    pass


# 5. Dependency helper to yield database sessions
# This function automatically handles opening and closing the database connection per request.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
