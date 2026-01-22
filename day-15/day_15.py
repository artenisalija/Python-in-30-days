# ================================
# DAY 15 - SIMPLE CRUD APP
# SQLAlchemy + PostgreSQL
# ================================

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# --------------------------------
# 1. CONNECT TO THE DATABASE
# --------------------------------
DATABASE_URL = "postgresql://user:1122@127.0.0.1:5432/day15"

# Create engine (connection to PostgreSQL)
engine = create_engine(DATABASE_URL)

# Session = how we talk to the database
SessionLocal = sessionmaker(bind=engine)

# Base class for all tables
Base = declarative_base()

# --------------------------------
# 2. DEFINE A TABLE (MODEL)
# --------------------------------
# This class becomes a table in PostgreSQL
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)   # Primary key column
    name = Column(String, nullable=False)    # Name column
    email = Column(String, nullable=False)   # Email column

# Create the table if it does not exist
Base.metadata.create_all(bind=engine)

# --------------------------------
# 3. OPEN A SESSION
# --------------------------------
db = SessionLocal()

# --------------------------------
# 4. CREATE (INSERT)
# --------------------------------
print("\n--- CREATE ---")

new_user = User(name="Artenis", email="art@example.com")

db.add(new_user)      # Prepare INSERT
db.commit()           # Execute INSERT
db.refresh(new_user) # Reload to get generated ID

print("Created user with ID:", new_user.id)

# --------------------------------
# 5. READ (SELECT)
# --------------------------------
print("\n--- READ ---")

users = db.query(User).all()   # SELECT * FROM users

for user in users:
    print(user.id, user.name, user.email)

# --------------------------------
# 6. UPDATE
# --------------------------------
print("\n--- UPDATE ---")

user_to_update = db.query(User).filter(User.name == "Artenis").first()

if user_to_update:
    user_to_update.name = "Updated Artenis"  # Change value
    db.commit()                               # Execute UPDATE
    print("Updated user name")

# --------------------------------
# 7. DELETE
# --------------------------------
print("\n--- DELETE ---")

user_to_delete = db.query(User).filter(User.name == "Updated Artenis").first()

if user_to_delete:
    db.delete(user_to_delete)   # Prepare DELETE
    db.commit()                 # Execute DELETE
    print("Deleted user")

# --------------------------------
# 8. CLOSE SESSION
# --------------------------------
db.close()
print("\nDone.")
