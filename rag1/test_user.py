from database import SessionLocal
from models import User

db = SessionLocal()

user = User(
    email="testg@gmail.com",
    password_hash="temporary_hash"
)

db.add(user)
db.commit()
db.refresh(user)

print(user.id)
print(user.email)

db.close()