import React from "react";
import { Link } from "react-router-dom";

const HomePage = () => {
  return (
    <div className="container mx-auto py-8 px-6">
      <h1 className="text-3xl font-bold text-gray-800 text-center mb-6">
        Quản Lý Chi Tiêu Cá Nhân
      </h1>
      <p className="text-center text-gray-600 mb-10">
        Chào mừng bạn đến với hệ thống quản lý chi tiêu cá nhân. Hãy bắt đầu
        theo dõi và quản lý mục tiêu tài chính của bạn!
      </p>

      {/* Các chức năng chính */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {/* Mục tiêu */}
        <Link
          to="/goals"
          className="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition duration-300"
        >
          <h2 className="text-xl font-semibold text-indigo-600 mb-4">
            Mục tiêu
          </h2>
          <p className="text-gray-700">
            Thiết lập và theo dõi các mục tiêu tài chính của bạn để đạt được mục
            tiêu tiết kiệm và chi tiêu hiệu quả.
          </p>
        </Link>

        {/* Giao dịch */}
        <Link
          to="/transactions"
          className="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition duration-300"
        >
          <h2 className="text-xl font-semibold text-indigo-600 mb-4">
            Giao dịch
          </h2>
          <p className="text-gray-700">
            Quản lý các giao dịch thu nhập và chi tiêu hàng ngày của bạn để duy
            trì ngân sách cá nhân.
          </p>
        </Link>

        {/* Báo cáo */}
        <Link
          to="/reports"
          className="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition duration-300"
        >
          <h2 className="text-xl font-semibold text-indigo-600 mb-4">
            Báo cáo
          </h2>
          <p className="text-gray-700">
            Xem các báo cáo chi tiêu và tiết kiệm để có cái nhìn tổng quan về
            tình hình tài chính của bạn.
          </p>
        </Link>
      </div>
    </div>
  );
};

export default HomePage;
