# app/models/goal_model.py
from . import db
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50))  # Thu nhập, Chi tiêu, Tiết kiệm
    description = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    # Reference
    goal_id = db.Column(UUID(as_uuid=True),
                        db.ForeignKey('goals.id'), nullable=True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'users.id'), nullable=False)
