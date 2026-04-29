from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime 

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


# class StudentCourse(Base):
#     __tablename__ = 'student_course'
#     id = Column(Integer, primary_key=True)
#     student_id = Column('student_id', Integer, ForeignKey('students.id'))
#     course_id = Column('course_id', Integer, ForeignKey('courses.id'))

# class Student(Base):
#     __tablename__ = 'students'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     courses = relationship("Course", secondary="student_course", back_populates="students")

# class Course(Base):
#     __tablename__ = 'courses'
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     students = relationship("Student", secondary="student_course", back_populates="courses")

# Base.metadata.create_all(engine)


# math = Course(title="Mathematics")
# physics = Course(title="Physics")
# bill = Student(name="Bill", courses=[math, physics])
# rob = Student(name="Rob", courses=[math])

# session.add_all([math, physics, bill, rob])
# session.commit()

# rob = session.query(Student).filter_by(name="Bill").first()
# courses = [courses.title for courses in rob.courses]
# print(f"Rob's courses: {', '.join(courses)}")

# class Appointment(Base):
#     __tablename__ = 'appointments'
#     id = Column(Integer, primary_key=True)
#     doctor_id = Column(Integer, ForeignKey('doctors.id'))
#     patient_id = Column(Integer, ForeignKey('patients.id'))
#     appointment_date = Column(DateTime, default=datetime.utcnow)
#     notes = Column(String)

#     doctor = relationship("Doctor", backref="appointments")
#     patient = relationship("Patient", backref="appointments")

# class Doctor(Base):
#     __tablename__ = 'doctors'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     specialty = Column(String) 


# class Patient(Base):
#     __tablename__ = 'patients'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     dob = Column(DateTime)

# Base.metadata.create_all(engine)

# dr_smith = Doctor(name="Dr. Smith", specialty="Cardiology")
# john_doe = Patient(name="John Doe", dob=datetime(1990, 1, 1))
# appointment = Appointment(doctor=dr_smith, patient=john_doe, notes='Routine check-up')

# session.add_all([dr_smith, john_doe, appointment])
# session.commit()

# appointments_for_dr_smith = session.query(Appointment).filter(Appointment.doctor.has(name="Dr. Smith")).all()


# print("Dr. Smith's appointments")
# print(appointments_for_dr_smith) 


class UserAssociation(Base):
    __tablename__ = 'user_associations'
    id = Column(Integer, primary_key=True)

    follower_id = Column(Integer, ForeignKey('users.id'))
    following_id = Column(Integer, ForeignKey('users.id'))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    following = relationship(
        'User',
        secondary='user_associations',
        primaryjoin="UserAssociation.follower_id == User.id",
        secondaryjoin="UserAssociation.following_id == User.id",
        backref='followers'
    )

    def __repr__(self):
        return f"<User: {self.name}>"
    
Base.metadata.create_all(engine)

user1 = User(name="John")
user2 = User(name="Rob")
user3 = User(name="Kyle")

user1.following.append(user2)
user2.following.append(user1)
user3.following.append(user1)

session.add_all([user1, user2, user3])
session.commit()    

print(f"{user1.name} is following {user1.following}")
print(f"{user1.name} is followed by {user1.followers}")
