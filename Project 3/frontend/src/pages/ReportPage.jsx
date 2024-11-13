// src/pages/ReportPage.js
import React, { useState, useEffect } from "react";
import { getTransactions } from "../service/api";
import { useAuth } from "../context/AuthProvider";

const ReportPage = () => {
  const [income, setIncome] = useState(0);
  const [expenses, setExpenses] = useState(0);
  const [savings, setSavings] = useState(0);
  const auth = useAuth();

  // Lấy và phân loại các giao dịch
  useEffect(() => {
    fetchReportData();
  }, []);

  const fetchReportData = async () => {
    try {
      const response = await getTransactions(auth.user.id);
      const transactions = response.data.data;

      let totalIncome = 0;
      let totalExpenses = 0;
      let totalSavings = 0;

      // Phân loại và tính toán tổng thu nhập, chi tiêu, tiết kiệm
      transactions.forEach((transaction) => {
        if (transaction.category === "Thu nhập") {
          totalIncome += transaction.amount;
        } else if (transaction.category === "Chi tiêu") {
          totalExpenses += transaction.amount;
        } else if (transaction.category === "Tiết kiệm") {
          totalSavings += transaction.amount;
        }
      });

      setIncome(totalIncome);
      setExpenses(totalExpenses);
      setSavings(totalSavings);
    } catch (error) {
      console.error("Error fetching report data:", error);
    }
  };

  return (
    <div className="container mx-auto py-8 px-6">
      <h1 className="text-3xl font-bold text-gray-800 text-center mb-6">
        Báo Cáo Tài Chính
      </h1>

      {/* Thông tin báo cáo tổng quan */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-6">
        <div className="bg-green-100 p-6 rounded-lg shadow-md text-center">
          <h2 className="text-xl font-semibold text-green-600 mb-2">
            Tổng Thu Nhập
          </h2>
          <p className="text-2xl font-bold text-green-700">
            {income.toLocaleString()} VND
          </p>
        </div>
        <div className="bg-red-100 p-6 rounded-lg shadow-md text-center">
          <h2 className="text-xl font-semibold text-red-600 mb-2">
            Tổng Chi Tiêu
          </h2>
          <p className="text-2xl font-bold text-red-700">
            {expenses.toLocaleString()} VND
          </p>
        </div>
        <div className="bg-blue-100 p-6 rounded-lg shadow-md text-center">
          <h2 className="text-xl font-semibold text-blue-600 mb-2">
            Tổng Tiết Kiệm
          </h2>
          <p className="text-2xl font-bold text-blue-700">
            {savings.toLocaleString()} VND
          </p>
        </div>
      </div>

      {/* Biểu đồ hoặc thống kê chi tiết hơn (tuỳ chọn) */}
      <div className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold text-indigo-600 mb-4">
          Phân Tích Chi Tiêu
        </h2>
        <p className="text-gray-600">
          Sử dụng biểu đồ hoặc thống kê chi tiết để theo dõi tình hình tài chính
          của bạn.
        </p>
        {/* Biểu đồ hoặc thống kê thêm ở đây nếu cần */}
      </div>
    </div>
  );
};

export default ReportPage;
