from models import session, User

#Creating users 
user1 = User(username="Van Dai 1")
user2 = User(username="Van Dai 2")
user3 = User(username="Van Dai 3")

#Creating relationships
user1.following.append(user2)
user2.following.append(user3)
user3.following.append(user1)

#Adding users to the session and committing the changes to the database
session.add_all([user1, user2, user3])
session.commit()

print(f"{user1.following = }")
print(f"{user2.following = }")
print(f"{user3.following = }")
