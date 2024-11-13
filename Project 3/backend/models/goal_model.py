# app/models/goal_model.py
from . import db
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Goal(db.Model):
    __tablename__ = 'goals'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(120), nullable=False)
    target_amount = db.Column(db.Float, nullable=False)
    saved_amount = db.Column(db.Float, default=0.0)
    description = db.Column(db.Text)
    deadline = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'users.id'), nullable=False)

    def progress(self):
        if self.target_amount == 0:
            return 0
        return min((self.saved_amount / self.target_amount) * 100, 100)
