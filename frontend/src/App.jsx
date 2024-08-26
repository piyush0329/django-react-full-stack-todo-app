import react from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import ProtectedRoute from "./components/ProtectedRoute";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import LoginForm from "./pages/LoginForm";
import RegisterForm from "./pages/RegisterFrom";

function Logout() {
  localStorage.clear();
  return <Navigate to="/login" />;
}

function RegisterAndLogout() {
  localStorage.clear();
  return <RegisterForm />;
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" 
        element={
          <ProtectedRoute>
            <Home/>
          </ProtectedRoute>
        } />
        <Route path="/login" element={<LoginForm/>} />
        <Route path="/logout" element={<Logout/>} />
        <Route path="/register" element={<RegisterAndLogout/>} />
        <Route path="*" element={<NotFound/>}/>
      </Routes>

    </BrowserRouter>
  );
}

export default App;
