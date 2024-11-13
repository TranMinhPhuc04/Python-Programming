// src/context/AuthProvider.js
import React, { createContext, useContext, useState } from "react";
import { loginUser } from "../service/api";

const AuthContext = createContext(null);

export const useAuth = () => {
  return useContext(AuthContext);
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(
    JSON.parse(localStorage.getItem("user")) || null
  );

  // Hàm đăng nhập
  const login = async (email, password) => {
    try {
      const response = await loginUser({ email, password });
      console.log(response);
      const { data } = response;
      
      // Lưu thông tin người dùng
      setUser(data.user);
      localStorage.setItem("user", JSON.stringify(data.user));
      return { success: true };
    } catch (error) {
      console.error("Login failed", error);
      return {
        success: false,
        message: error.response?.data?.message || "Login failed",
      };
    }
  };

  // Hàm đăng xuất
  const logout = () => {
    setUser(null);
    localStorage.removeItem("user");
  };

  const value = {
    user,
    login,
    logout,
    isAuthenticated: !!user,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
