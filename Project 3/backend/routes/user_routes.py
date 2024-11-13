# app/routes/user_routes.py
from flask import Blueprint, jsonify, request
from models import db
from models.user_model import User
import bcrypt

user_api = Blueprint('user_api', __name__)



# Đăng ký người dùng mới


@user_api.route('/register', methods=['POST'])
def register():
    data = request.json
    # Hash mật khẩu bằng bcrypt
    hashed_password = bcrypt.hashpw(
        data['password'].encode('utf-8'), bcrypt.gensalt())
    new_user = User(
        username=data['username'], email=data['email'], password_hash=hashed_password.decode(
            'utf-8')
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully."}), 201


@user_api.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    # Kiểm tra xem user có tồn tại và mật khẩu có khớp không
    if not user or not bcrypt.checkpw(data['password'].encode('utf-8'), user.password_hash.encode('utf-8')):
        return jsonify({"message": "Invalid credentials"}), 401

    # Trả về dữ liệu người dùng sau khi đăng nhập thành công
    user_data = {
        "id": str(user.id),         # Chuyển UUID thành chuỗi (nếu dùng UUID)
        "username": user.username,
        "email": user.email
    }
    return jsonify({"message": "Login successful", "user": user_data}), 200
