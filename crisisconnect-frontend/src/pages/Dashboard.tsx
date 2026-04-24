import { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import EmergencyCard from "../components/EmergencyCard";
import toast from "react-hot-toast";
import api from "../services/api"; // ✅ IMPORTANT

type Alert = {
  id: string;
  type: string;
  message: string;
  timestamp: string;
  status: string;
};

const Dashboard = () => {
  const [message, setMessage] = useState("");
  const [alerts, setAlerts] = useState<Alert[]>([]);
  const [loading, setLoading] = useState(false);

  // 🔥 FETCH ALERTS FROM BACKEND
  const fetchAlerts = async () => {
    try {
      const res = await api.get("/emergency/get-alerts");
      setAlerts(res.data);
    } catch (err) {
      toast.error("Failed to fetch alerts");
    }
  };

  // 🔁 AUTO LOAD
  useEffect(() => {
    fetchAlerts();

    const interval = setInterval(fetchAlerts, 5000);
    return () => clearInterval(interval);
  }, []);

  // 🚨 REPORT (API)
  const handleReport = async () => {
    if (!message) {
      toast.error("Enter message");
      return;
    }

    try {
      setLoading(true);

      await api.post("/emergency/report-emergency", {
        message,
      });

      toast.success("Emergency reported!");
      setMessage("");

      fetchAlerts(); // 🔥 refresh
    } catch (err) {
      toast.error("Failed to report");
    } finally {
      setLoading(false);
    }
  };

  // ✅ RESOLVE (API)
  const handleResolve = async (id: string) => {
    try {
      await api.put(`/emergency/update-status/${id}`, {
        status: "Resolved",
      });

      toast.success("Updated!");
      fetchAlerts();
    } catch (err) {
      toast.error("Failed to update");
    }
  };

  // 📊 STATS
  const activeCount = alerts.filter(a => a.status === "Active").length;
  const resolvedCount = alerts.filter(a => a.status === "Resolved").length;
  const totalCount = alerts.length;

  return (
    <div className="bg-gray-50 min-h-screen">
      <Navbar />

      <div className="p-6 max-w-7xl mx-auto">

        {/* REPORT BOX */}
        <div className="bg-[#1e293b] p-6 rounded-2xl mb-8 shadow-md border border-gray-700">
          <h2 className="text-white text-lg mb-4 font-semibold">
            🚨 Report Emergency
          </h2>

          <div className="flex gap-4">
            <input
              type="text"
              placeholder="Describe emergency..."
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              className="flex-1 p-3 rounded-xl bg-[#0f172a] border border-gray-600 text-white outline-none focus:ring-2 focus:ring-blue-500"
            />

            <button
              onClick={handleReport}
              className="bg-gradient-to-r from-red-500 to-pink-500 px-5 py-2 rounded-xl text-white hover:scale-105 transition"
            >
              {loading ? "Sending..." : "Report"}
            </button>
          </div>
        </div>

        {/* STATS */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="bg-white p-5 rounded-2xl shadow-sm border">
            <p className="text-gray-500 text-sm">Active</p>
            <h2 className="text-3xl font-bold text-blue-600">{activeCount}</h2>
          </div>

          <div className="bg-white p-5 rounded-2xl shadow-sm border">
            <p className="text-gray-500 text-sm">Resolved</p>
            <h2 className="text-3xl font-bold text-green-600">{resolvedCount}</h2>
          </div>

          <div className="bg-white p-5 rounded-2xl shadow-sm border">
            <p className="text-gray-500 text-sm">Total</p>
            <h2 className="text-3xl font-bold text-purple-600">{totalCount}</h2>
          </div>
        </div>

        {/* TITLE */}
        <h2 className="text-xl font-semibold text-gray-700 mb-4">
          🚨 Recent Alerts
        </h2>

        {/* ALERTS */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {alerts.length === 0 ? (
            <div className="text-center mt-20 text-gray-400 col-span-full">
              <p className="text-3xl">🚀</p>
              <p className="mt-2 text-lg">No emergencies yet</p>
            </div>
          ) : (
            alerts.map((alert) => (
              <EmergencyCard
                key={alert.id}
                alert={alert}
                onResolve={handleResolve}
              />
            ))
          )}
        </div>

      </div>
    </div>
  );
};

export default Dashboard;