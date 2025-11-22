from sqlalchemy import Column, Integer, String,Text, Boolean
from app.database import Base, engine


# class Product(Base):
#     __tablename__ = "product"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     image = Column(String)
#     title = Column(String, nullable=False)
#     about = Column(String)
#     price = Column(NUMERIC(9, 2))
#     review = Column(Integer,
#                     CheckConstraint('review BETWEEN 1 AND 5'),
#                     default=1)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    gmail = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    confirm_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)


class Contact(Base):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True, autoincrement=True)
    your_name = Column(String, nullable=False, unique=True)
    gmail = Column(String, nullable=False, unique=True)
    subject = Column(String, nullable=False)
    message = Column(Text)



class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(String, nullable=False, unique=True)
    course_name = Column(String, nullable=False)
    about = Column(String, nullable=False)
    age_limit = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

Base.metadata.create_all(engine)
