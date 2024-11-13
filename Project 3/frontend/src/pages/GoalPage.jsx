// src/pages/GoalPage.js
import React, { useState, useEffect } from "react";
import { getGoals, createGoal, updateGoal, deleteGoal } from "../service/api";
import { useAuth } from "../context/AuthProvider";

const GoalPage = () => {
  const [goals, setGoals] = useState([]);
  const [editingGoal, setEditingGoal] = useState(null);
  const [name, setName] = useState("");
  const [targetAmount, setTargetAmount] = useState("");
  const [description, setDescription] = useState("");
  const auth = useAuth();

  // Lấy danh sách mục tiêu khi trang được tải
  useEffect(() => {
    fetchGoals();
  }, []);

  const fetchGoals = async () => {
    try {
      const response = await getGoals(auth.user.id);
      setGoals(response.data.data);
    } catch (error) {
      console.error("Error fetching goals:", error);
    }
  };

  // Xử lý thêm hoặc cập nhật mục tiêu
  const handleSaveGoal = async (e) => {
    e.preventDefault();
    const goalData = {
      name,
      target_amount: targetAmount,
      description,
      user_id: auth.user.id,
    };

    try {
      if (editingGoal) {
        await updateGoal(editingGoal.id, goalData);
        setEditingGoal(null);
      } else {
        await createGoal(goalData);
      }
      setName("");
      setTargetAmount("");
      setDescription("");
      fetchGoals();
    } catch (error) {
      console.error("Error saving goal:", error);
    }
  };

  // Xử lý chỉnh sửa mục tiêu
  const handleEditGoal = (goal) => {
    setEditingGoal(goal);
    setName(goal.name);
    setTargetAmount(goal.target_amount);
    setDescription(goal.description);
  };

  // Xử lý xóa mục tiêu
  const handleDeleteGoal = async (goalId) => {
    try {
      await deleteGoal(goalId);
      fetchGoals();
    } catch (error) {
      console.error("Error deleting goal:", error);
    }
  };

  return (
    <div className="container mx-auto py-8 px-6">
      <h1 className="text-3xl font-bold text-gray-800 text-center mb-6">
        Mục Tiêu Tài Chính
      </h1>

      {/* Form thêm/sửa mục tiêu */}
      <form
        onSubmit={handleSaveGoal}
        className="bg-white p-6 rounded-lg shadow-md mb-6"
      >
        <h2 className="text-xl font-semibold text-indigo-600 mb-4">
          {editingGoal ? "Chỉnh Sửa Mục Tiêu" : "Thêm Mục Tiêu"}
        </h2>
        <input
          type="text"
          placeholder="Tên mục tiêu"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="w-full mb-4 px-4 py-2 border border-gray-300 rounded-md"
        />
        <input
          type="number"
          placeholder="Số tiền cần đạt"
          value={targetAmount}
          onChange={(e) => setTargetAmount(e.target.value)}
          className="w-full mb-4 px-4 py-2 border border-gray-300 rounded-md"
        />
        <textarea
          placeholder="Mô tả (tuỳ chọn)"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="w-full mb-4 px-4 py-2 border border-gray-300 rounded-md"
        ></textarea>
        <button
          type="submit"
          className="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 transition"
        >
          {editingGoal ? "Lưu Thay Đổi" : "Thêm Mục Tiêu"}
        </button>
      </form>

      {/* Danh sách mục tiêu */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {goals.map((goal) => (
          <div key={goal.id} className="bg-white p-6 rounded-lg shadow-md">
            <h3 className="text-xl font-semibold text-gray-800">{goal.name}</h3>
            <p className="text-gray-600">
              Số tiền cần đạt: {goal.target_amount}
            </p>
            <p className="text-gray-500">{goal.description}</p>
            <div className="mt-4 flex space-x-4">
              <button
                onClick={() => handleEditGoal(goal)}
                className="text-indigo-600 hover:underline"
              >
                Chỉnh sửa
              </button>
              <button
                onClick={() => handleDeleteGoal(goal.id)}
                className="text-red-500 hover:underline"
              >
                Xóa
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default GoalPage;
