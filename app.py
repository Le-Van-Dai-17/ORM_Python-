from sqlalchemy.orm import sessionmaker 

from models import User, engine 

Session = sessionmaker(bind=engine)

session = Session()

# user = User(name="John Doe", age=30)
# user_2 = User(name="Andrew Pip", age=25)
# user_3 = User(name="Iron Man", age=57)
# user_4 = User(name="Richard Rodriguez", age=25)

# session.add(user_2)
# session.add_all([user_3, user_4])

# session.commit()

# users = session.query(User).filter_by(id=1).all()

# print(user)

# print(user[0])

# print(user[0].id)
# print(user[0].name)
# print(user[0].age)

# for user in users:
    # print(f"User ID: {user.id}, name: {user.name}, age: {user.age}")


user = session.query(User).filter_by(id=1).one_or_none()

# print(user.name)

# user.name = "A different name"

# print(user.name)

# session.commit()

session.delete(user)

session.commit()