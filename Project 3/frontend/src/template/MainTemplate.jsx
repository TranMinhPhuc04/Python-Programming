import React from "react";
import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../context/AuthProvider";
import Header from "../components/Header";
import Footer from "../components/Footer";

const MainTemplate = () => {
  const auth = useAuth();

  if (!auth.isAuthenticated) {
    return <Navigate to="/login" />;
  }

  return (
    <>
      <header>
        <Header />
      </header>

      <main className="container mx-auto my-8 px-6 " style={{ height: "80vh" }}>
        <Outlet />
      </main>

      <footer>
        <Footer />
      </footer>
    </>
  );
};

export default MainTemplate;
