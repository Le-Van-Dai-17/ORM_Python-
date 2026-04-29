from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base 

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     address = relationship("Address", back_populates="user", uselist=False)

# class Address(Base):
#     __tablename__ = "addresses"
#     id = Column(Integer, primary_key=True)
#     email = Column(String, unique=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     user = relationship("User", back_populates="address")

Base.metadata.create_all(engine)

# new_user = User(name="John Doe")
# new_address = Address(email="john@example.com", user=new_user)

# session.add(new_user)
# session.add(new_address)
# session.commit()


# print(new_user.name)
# print(new_address.email)
# print(new_user.address.email)
# print(new_address.user.name)


# user = session.query(User).filter_by(name="John Doe").first()
# print(f"User: {user.name}, Email: {user.address.email}")


class NodeAssociation(Base):
    __tablename__ = "node_association"
    id = Column(Integer, primary_key=True)

    current_node_id = Column(Integer, ForeignKey("nodes.id"))
    next_node_id = Column(Integer, ForeignKey("nodes.id"))


class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)

    next_node = relationship(
        "Node",
        secondary="node_association",
        primaryjoin="NodeAssociation.current_node_id == Node.id",
        secondaryjoin="NodeAssociation.next_node_id == Node.id",
        uselist=False
    )

    def __repr__(self):
        return f"<Node value={self.value}>"
    
Base.metadata.create_all(engine)

node1 = Node(value=1)
node2 = Node(value=2)
node3 = Node(value=3)

node1.next_node = node2
node2.next_node = node3
node3.next_node = node1

session.add_all([node1, node2, node3])
session.commit()

print(node1)
print(node2)
print(node3)
