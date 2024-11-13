# app/routes/goal_routes.py
from flask import Blueprint, jsonify, request
from models import db
from models.goal_model import Goal
from flask_cors import CORS

goal_api = Blueprint('goal_api', __name__)

CORS(goal_api)
# Tạo mục tiêu mới


@goal_api.route('/', methods=['POST'])
def create_goal():
    data = request.json
    new_goal = Goal(
        name=data['name'],
        target_amount=data['target_amount'],
        description=data.get('description', ''),
        deadline=data.get('deadline'),
        user_id=data['user_id']
    )
    db.session.add(new_goal)
    db.session.commit()
    return jsonify({
        "success": True,
        "message": "Goal created successfully",
        "data": {
            "id": str(new_goal.id),
            "name": new_goal.name,
            "target_amount": new_goal.target_amount,
            "description": new_goal.description,
            "deadline": new_goal.deadline,
            "user_id": str(new_goal.user_id)
        }
    }), 201

# Lấy danh sách các mục tiêu của người dùng


@goal_api.route('/<uuid:user_id>', methods=['GET'])
def get_goals(user_id):
    goals = Goal.query.filter_by(user_id=user_id).all()
    goals_data = [
        {
            "id": str(goal.id),
            "name": goal.name,
            "target_amount": goal.target_amount,
            "description": goal.description,
            "deadline": goal.deadline,
            "user_id": str(goal.user_id)
        }
        for goal in goals
    ]
    return jsonify({
        "success": True,
        "message": "Goals retrieved successfully",
        "data": goals_data
    }), 200

# Cập nhật mục tiêu


@goal_api.route('/<uuid:goal_id>', methods=['PUT'])
def update_goal(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    data = request.json
    goal.name = data.get('name', goal.name)
    goal.target_amount = data.get('target_amount', goal.target_amount)
    goal.description = data.get('description', goal.description)
    goal.deadline = data.get('deadline', goal.deadline)
    db.session.commit()
    return jsonify({
        "success": True,
        "message": "Goal updated successfully",
        "data": {
            "id": str(goal.id),
            "name": goal.name,
            "target_amount": goal.target_amount,
            "description": goal.description,
            "deadline": goal.deadline,
            "user_id": str(goal.user_id)
        }
    }), 200

# Xóa mục tiêu


@goal_api.route('/<uuid:goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    db.session.delete(goal)
    db.session.commit()
    return jsonify({
        "success": True,
        "message": "Goal deleted successfully"
    }), 200
