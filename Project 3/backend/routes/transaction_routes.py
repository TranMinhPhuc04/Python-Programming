# app/routes/transaction_routes.py
from flask import Blueprint, jsonify, request
from models import db
from models.transaction_model import Transaction
from models.goal_model import Goal

transaction_api = Blueprint('transaction_api', __name__)

# Tạo giao dịch mới


@transaction_api.route('', methods=['POST'])
def create_transaction():
    data = request.json
    new_transaction = Transaction(
        amount=data['amount'],
        category=data['category'],
        description=data.get('description', ''),
        goal_id=data.get('goal_id'),
        user_id=data['user_id']
    )
    db.session.add(new_transaction)
    db.session.commit()

    # Nếu là tiết kiệm cho mục tiêu, cập nhật số tiền tiết kiệm trong Goal
    if data['category'] == 'Tiết kiệm' and data.get('goal_id'):
        goal = Goal.query.get(data['goal_id'])
        if goal:
            goal.saved_amount += data['amount']
            db.session.commit()

    return jsonify({
        "success": True,
        "message": "Transaction created successfully",
        "data": {
            "id": str(new_transaction.id),
            "amount": new_transaction.amount,
            "category": new_transaction.category,
            "description": new_transaction.description,
            "goal_id": str(new_transaction.goal_id) if new_transaction.goal_id else None,
            "user_id": str(new_transaction.user_id)
        }
    }), 201

# Lấy danh sách giao dịch của người dùng


@transaction_api.route('/<uuid:user_id>', methods=['GET'])
def get_transactions(user_id):
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    transactions_data = [
        {
            "id": str(transaction.id),
            "amount": transaction.amount,
            "category": transaction.category,
            "description": transaction.description,
            "goal_id": str(transaction.goal_id) if transaction.goal_id else None,
            "user_id": str(transaction.user_id)
        }
        for transaction in transactions
    ]
    return jsonify({
        "success": True,
        "message": "Transactions retrieved successfully",
        "data": transactions_data
    }), 200
