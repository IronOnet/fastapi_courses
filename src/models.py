from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Enum,
    ForeignKey,
    Text,
    Date,
    Double,
)
from sqlalchemy.orm import relationship

from db.base import Base, engine


class User(Base):
    __tablename__ = "users"
    id = Column(String(30), primary_key=True, autoincrement=True)
    username = Column(String(30), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(30))
    last_name = Column(String(20))
    password_hash = Column(String(30))
    role = Column(Enum("student", "instructor", "administrator"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), unique=True, nullable=False)
    description = Column(String(30))
    duration = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    instructor = Column(Integer, ForeignKey("instructors.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    instructor_rel = relationship("Instructor", back_populates="courses")


class Instructor(Base):
    __tablename__ = "instructors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


class Module(Base):
    __tablename__ = "modules"
    module_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    duration = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    materials_id = Column(Integer, ForeignKey("materials.id"))
    material_rel = relationship("Material", back_populates="module_rel")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))
    description = Column(String(255))
    course_id = Column(Integer, ForeignKey("courses.id"))
    due_date = Column(Date)
    total_points = Column(Double)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user_rel = relationship("User", back_populates="students_rel")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    course_rel = relationship("Course", back_populates="enrollments")
    student_rel = relationship("Student", back_populates="enrollments")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String(30))
    description = Column(Text)
    file_path = Column(String(200))
    url = Column(String(200))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


Base.metadata.create_all(engine)
