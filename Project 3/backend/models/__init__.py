from flask_sqlalchemy import SQLAlchemy

# Khởi tạo SQLAlchemy instance
db = SQLAlchemy()

# Import các model để sử dụng khi khởi động ứng dụng
from .user_model import User
from .goal_model import Goal
from .transaction_model import Transaction
