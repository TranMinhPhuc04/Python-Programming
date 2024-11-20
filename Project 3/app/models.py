from app import db
from sqlalchemy import CheckConstraint


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Student(db.Model):
    __tablename__ = 'students'
    mssv = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    major = db.Column(db.String, nullable=True)
    enrollments = db.relationship('Enrollment', backref='student', lazy=True)


class Course(db.Model):
    __tablename__ = 'courses'
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String, unique=True, nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    enrollments = db.relationship('Enrollment', backref='course', lazy=True)
    # Thêm ràng buộc kiểm tra cho số tín chỉ
    __table_args__ = (
        CheckConstraint('credits > 0', name='check_credits_positive'),
    )


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    enrollment_id = db.Column(db.Integer, primary_key=True)
    student_mssv = db.Column(db.String, db.ForeignKey(
        'students.mssv'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'courses.course_id'), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False)
