# app/models/user_model.py
from . import db
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    # Reference
    goals = db.relationship('Goal', backref='user', lazy=True)
    transactions = db.relationship('Transaction', backref='user', lazy=True)
