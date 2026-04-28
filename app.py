import random 

from sqlalchemy.orm import sessionmaker 

from models import User, engine 

Session = sessionmaker(bind=engine)

session = Session()

# names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# ages = [25, 30, 35, 40, 45]

# for x in range(20):
#     user = User(name=random.choice(names), age=random.choice(ages))
#     session.add(user)

# session.commit()

#Query all users ordered by age (ascending) 
users = session.query(User).order_by(User.age.desc(), User.name).all()

for user in users:
    print(f"Use age: {user.age}, name: {user.name}, id: {user.id}")
