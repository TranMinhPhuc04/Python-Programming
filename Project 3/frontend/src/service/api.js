// src/services/api.js
import axios from "axios";

const API_BASE_URL = "http://localhost:5000";

// Cấu hình Axios với base URL cho các API endpoint
const api = axios.create({
  baseURL: API_BASE_URL,
});

// 1. Các API liên quan đến người dùng (User)

// Đăng ký người dùng mới
export const createUser = (userData) => api.post("/user/register", userData);

// Đăng nhập người dùng
export const loginUser = (loginData) => api.post("/user/login", loginData);

// 2. Các API liên quan đến mục tiêu (Goal)

// Lấy danh sách mục tiêu của người dùng
export const getGoals = (userId) => api.get(`/goal/${userId}`);

// Tạo một mục tiêu mới
export const createGoal = (goalData) =>
  api.post("/goal", goalData, {
    headers: {
      "Content-Type": "application/json",
    },
  });

// Cập nhật mục tiêu
export const updateGoal = (goalId, goalData) =>
  api.put(`/goal/${goalId}`, goalData);

// Xóa mục tiêu
export const deleteGoal = (goalId) => api.delete(`/goal/${goalId}`);

// 3. Các API liên quan đến giao dịch (Transaction)

// Lấy danh sách giao dịch của người dùng
export const getTransactions = (userId) => api.get(`/transaction/${userId}`);

// Tạo một giao dịch mới
export const createTransaction = (transactionData) =>
  api.post("/transaction", transactionData);
