#Task 1 
#Add models for student, subject and student_subject from previous lessons in SQLAlchemy.

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'Student'
    student_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Student(name='{self.name}', age={self.age})>"

class Subject(Base):
    __tablename__ = 'Subject'
    subject_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    length = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Subject(name='{self.name}', length={self.length})>"

class StudentSubject(Base):
    __tablename__ = 'Student_Subject'
    student_subject_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('Student.student_id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('Subject.subject_id'), nullable=False)

    # Defining the relationships
    student = relationship("Student", back_populates="subjects")
    subject = relationship("Subject", back_populates="students")

    def __repr__(self):
        return f"<StudentSubject(student_id={self.student_id}, subject_id={self.subject_id})>"

# Here 'database_url' should be replaces with the actual database connection URL
engine = create_engine('database_url')

# Creation of a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Task 2.
# Find all students` name that visited 'English' classes
students_with_english = session.query(Student.name).join(StudentSubject).join(Subject).filter(Subject.name == 'English').all()

# Extraction the names from the result
student_names = [student[0] for student in students_with_english]

# Printing the names
print(student_names)