import random 

from sqlalchemy import func
from sqlalchemy.orm import sessionmaker 

from models import User, engine 

Session = sessionmaker(bind=engine)

session = Session()

#group user by age 
# users = session.query(User.age, func.count(User.id)).group_by(User.age).all()

# print(users)

# users_tuple = (
    # session.query(User.age, func.count(User.id))
#     # .filter(User.age > 30)
#     .filter(User.age < 50)
#     .group_by(User.age)
#     .order_by(User.age)
#     .all()
# )

# for user in users_tuple:
#     print(f"Age: {user[0]}, count: {user[1]}")


only_alice = True 
group_by_age = True 


users = session.query(User)

if only_alice:
    users = users.filter(User.name == "Alice")

if group_by_age: 
    users = users.group_by(User.age)

users = users.all()

for user in users:
    print(f"Name: {user.name}, Age: {user.age}")