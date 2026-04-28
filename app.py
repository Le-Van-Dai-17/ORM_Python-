import random 

from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker 

from models import User, engine 

Session = sessionmaker(bind=engine)

session = Session()

#query all users 
# users_all = session.query(User).all()

# users_filtered = session.query(User).filter(User.age > 25).all()

# users_filtered = session.query(User).filter(User.age >= 25, User.name == "Alice").all()

# print("All users: ", len(users_all))
# print("Filtered users: ", len(users_filtered))


# users = session.query(User).filter_by(age = 30).all()

# for user in users:
    # print(f"User: {user.name}, age: {user.age}")

# users = session.query(User).where(User.age >= 30).all()

# for user in users:
    # print(f"User: {user.name}, age: {user.age}")

# users = session.query(User).where(or_(User.age >= 30, User.name == "Alice")).all()
users = session.query(User).where((User.age >= 30) | (User.name == "Alice")).all()

for user in users:
    print(f"User: {user.name}, age: {user.age}")