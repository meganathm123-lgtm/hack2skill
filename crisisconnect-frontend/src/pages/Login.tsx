import { useState } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";
import api from "../services/api"; // ✅ FIXED

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const params = new URLSearchParams();
      params.append("username", email);
      params.append("password", password);

      const res = await api.post("/auth/login", params, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });

      const token = res.data.access_token;

      localStorage.setItem("token", token);

      toast.success("Login successful!");
      navigate("/");
    } catch (err) {
      console.log(err);
      toast.error("Login failed");
    }
  };

  return (
    <div className="h-screen grid grid-cols-2">

      {/* LEFT SIDE */}
      <div className="bg-gradient-to-br from-blue-600 to-indigo-600 text-white flex flex-col justify-center items-center p-10">
        <h1 className="text-4xl font-bold mb-4">
          CrisisConnect AI 🚨
        </h1>
        <p className="text-lg text-blue-100 text-center max-w-md">
          Smart emergency response system for faster, safer hospitality management.
        </p>
      </div>

      {/* RIGHT SIDE */}
      <div className="flex items-center justify-center bg-gray-50">
        <div className="bg-white p-8 rounded-2xl w-96 shadow-xl border">

          <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">
            Welcome Back 👋
          </h2>

          <input
            type="text"
            placeholder="Username"
            className="w-full mb-4 p-3 rounded-xl border bg-gray-100"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <input
            type="password"
            placeholder="Password"
            className="w-full mb-6 p-3 rounded-xl border bg-gray-100"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button
            onClick={handleLogin}
            className="w-full py-3 rounded-xl text-white bg-gradient-to-r from-blue-500 to-indigo-500 hover:scale-105 transition"
          >
            Login
          </button>

          <p className="text-sm text-center mt-4 text-gray-500">
            Don’t have an account?{" "}
            <span
              className="text-blue-500 cursor-pointer"
              onClick={() => navigate("/register")}
            >
              Register
            </span>
          </p>

        </div>
      </div>

    </div>
  );
};

export default Login;