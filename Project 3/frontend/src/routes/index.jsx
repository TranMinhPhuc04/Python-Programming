// src/routes/index.js
import { Route } from "react-router-dom";
import MainTemplate from "../template/MainTemplate";
import LoginPage from "../pages/LoginPage";
import RegisterPage from "../pages/RegisterPage";
import HomePage from "../pages/HomePage";
import GoalPage from "../pages/GoalPage";
import TransactionPage from "../pages/TransactionPage";
import ReportPage from "../pages/ReportPage";

const routes = [
  {
    path: "/",
    element: MainTemplate,
    children: [
      {
        index: true,
        path: "",
        element: HomePage,
      },
      {
        path: "/goals",
        element: GoalPage,
      },
      {
        path: "/transactions",
        element: TransactionPage,
      },
      {
        path: "/reports",
        element: ReportPage,
      },
    ],
  },
  {
    path: "/login",
    element: LoginPage,
  },
  {
    path: "/register",
    element: RegisterPage,
  },
];

const renderRoutes = () => {
  return routes.map((route) => {
    if (route.children) {
      return (
        <Route key={route.path} path={route.path} element={<route.element />}>
          {route.children.map((item) => (
            <Route
              key={item.path}
              path={item.path}
              element={<item.element />}
            />
          ))}
        </Route>
      );
    } else {
      return (
        <Route key={route.path} path={route.path} element={<route.element />} />
      );
    }
  });
};

export default renderRoutes;
