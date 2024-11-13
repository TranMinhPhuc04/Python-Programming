import React from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthProvider";

const Header = () => {
  const auth = useAuth();
  return (
    <header className="bg-indigo-600 text-white shadow-md">
      <div className="container mx-auto flex items-center justify-between py-4 px-6">
        <h1 className="text-2xl font-semibold">
          <Link to="/">Chi Tieu</Link>
        </h1>
        <nav className="flex space-x-4">
          <Link to="/goals" className="hover:underline">
            Mục tiêu
          </Link>
          <Link to="/transactions" className="hover:underline">
            Giao dịch
          </Link>
          <Link to="/reports" className="hover:underline">
            Báo cáo
          </Link>
          <button
            onClick={auth.logout}
            className="bg-red-500 px-3 py-1 rounded-md hover:bg-red-600 transition"
          >
            Đăng xuất
          </button>
        </nav>
      </div>
    </header>
  );
};

export default Header;
