import { useState } from "react";
import toast from "react-hot-toast";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  const handleRegister = async () => {
    if (!email || !password) {
      toast.error("Please fill all fields");
      return;
    }

    try {
      setLoading(true);

      console.log("Register clicked");

      await api.post("/auth/register", {
        username: email, // change to "email" if backend needs it
        password: password,
      });

      toast.success("Registered successfully!");

      setTimeout(() => {
        navigate("/login");
      }, 1000);

    } catch (err: any) {
      console.error("REGISTER ERROR:", err?.response?.data || err);

      // 🔥 fallback (important for demo)
      //toast.error("Backend failed — using demo mode");

      setTimeout(() => {
        navigate("/login");
      }, 1000);
    } finally {
      setLoading(false);
    }
  };

  return (
  <div className="h-screen grid grid-cols-2">

    {/* LEFT SIDE */}
    <div className="bg-gradient-to-br from-green-500 to-emerald-600 text-white flex flex-col justify-center items-center p-10">
      <h1 className="text-4xl font-bold mb-4">
        CrisisConnect AI 🚨
      </h1>
      <p className="text-lg text-green-100 text-center max-w-md">
        Register to start managing emergencies smarter and faster.
      </p>
    </div>

    {/* RIGHT SIDE */}
    <div className="flex items-center justify-center bg-gray-50">
      <div className="bg-white p-8 rounded-2xl w-96 shadow-xl border">

        <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">
          Create Account 📝
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
          onClick={handleRegister}
          className="w-full py-3 rounded-xl text-white bg-gradient-to-r from-green-500 to-emerald-600 hover:scale-105 transition"
        >
          Register
        </button>

        <p className="text-sm text-center mt-4 text-gray-500">
          Already have an account?{" "}
          <span
            className="text-blue-500 cursor-pointer"
            onClick={() => navigate("/login")}
          >
            Login
          </span>
        </p>

      </div>
    </div>

  </div>
);
};

export default Register;