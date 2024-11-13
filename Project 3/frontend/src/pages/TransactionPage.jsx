// src/pages/TransactionPage.js
import React, { useState, useEffect } from "react";
import {
  getTransactions,
  createTransaction,
  // deleteTransaction,
} from "../service/api";
import { useAuth } from "../context/AuthProvider";

const TransactionPage = () => {
  const [transactions, setTransactions] = useState([]);
  const [amount, setAmount] = useState("");
  const [category, setCategory] = useState("Chi tiêu");
  const [description, setDescription] = useState("");
  const [goalId, setGoalId] = useState(null);
  const auth = useAuth();

  // Lấy danh sách giao dịch khi trang được tải
  useEffect(() => {
    fetchTransactions();
  }, []);

  const fetchTransactions = async () => {
    try {
      const response = await getTransactions(auth.user.id);
      setTransactions(response.data.data);
    } catch (error) {
      console.error("Error fetching transactions:", error);
    }
  };

  // Xử lý thêm giao dịch
  const handleSaveTransaction = async (e) => {
    e.preventDefault();
    const transactionData = {
      amount: parseFloat(amount),
      category,
      description,
      user_id: auth.user.id,
      goal_id: goalId || null,
    };

    try {
      await createTransaction(transactionData);
      setAmount("");
      setCategory("Chi tiêu");
      setDescription("");
      setGoalId(null);
      fetchTransactions();
    } catch (error) {
      console.error("Error saving transaction:", error);
    }
  };

  // Xử lý xóa giao dịch
  // const handleDeleteTransaction = async (transactionId) => {
  //   try {
  //     await deleteTransaction(transactionId);
  //     fetchTransactions();
  //   } catch (error) {
  //     console.error("Error deleting transaction:", error);
  //   }
  // };

  return (
    <div className="container mx-auto py-8 px-6">
      <h1 className="text-3xl font-bold text-gray-800 text-center mb-6">
        Quản Lý Giao Dịch
      </h1>

      {/* Form thêm giao dịch */}
      <form
        onSubmit={handleSaveTransaction}
        className="bg-white p-6 rounded-lg shadow-md mb-6"
      >
        <h2 className="text-xl font-semibold text-indigo-600 mb-4">
          Thêm Giao Dịch
        </h2>
        <input
          type="number"
          placeholder="Số tiền"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          className="w-full mb-4 px-4 py-2 border border-gray-300 rounded-md"
        />
        <select
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          className="w-full mb-4 px-4 py-2 border border-gray-300 rounded-md"
        >
          <option value="Chi tiêu">Chi tiêu</option>
          <option value="Thu nhập">Thu nhập</option>
          <option value="Tiết kiệm">Tiết kiệm</option>
        </select>
        <textarea
          placeholder="Mô tả giao dịch"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="w-full mb-4 px-4 py-2 border border-gray-300 rounded-md"
        ></textarea>
        <button
          type="submit"
          className="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 transition"
        >
          Thêm Giao Dịch
        </button>
      </form>

      {/* Danh sách giao dịch */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {transactions.map((transaction) => (
          <div
            key={transaction.id}
            className="bg-white p-6 rounded-lg shadow-md"
          >
            <h3 className="text-xl font-semibold text-gray-800">
              {transaction.category}: {transaction.amount} VND
            </h3>
            <p className="text-gray-500">{transaction.description}</p>
            <div className="mt-4 flex justify-end space-x-4">
              <button
                // onClick={() => handleDeleteTransaction(transaction.id)}
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

export default TransactionPage;
