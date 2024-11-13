import React from "react";

const Footer = () => {
  return (
    <footer className="bg-gray-800 text-gray-400">
      <div className="container mx-auto py-4 px-6 text-center">
        <p>
          &copy; {new Date().getFullYear()} Quản Lý Chi Tiêu. All rights
          reserved.
        </p>
      </div>
    </footer>
  );
};

export default Footer;
