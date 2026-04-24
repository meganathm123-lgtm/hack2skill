import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext"; // make sure path is correct
import toast from "react-hot-toast";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleLogin = async () => {
    if (!email || !password) {
      toast.error("Enter credentials");
      return;
    }

    try {
      // ✅ MOCK LOGIN (frontend only)
      const fakeToken = "demo_token";

      localStorage.setItem("token", fakeToken);
      login(fakeToken); // update context

      toast.success("Login successful!");

      setTimeout(() => {
        navigate("/");
      }, 1000);

    } catch (err) {
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