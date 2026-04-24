import { Flame, ShieldAlert, HeartPulse } from "lucide-react";

type Alert = {
  id: string;
  type: string;
  message: string;
  timestamp: string;
  status: string;
};

// 🔥 ICON
const getIcon = (type: string) => {
  const t = type?.toLowerCase();

  if (t === "fire") return <Flame className="text-red-500 w-5 h-5" />;
  if (t === "medical") return <HeartPulse className="text-green-500 w-5 h-5" />;
  return <ShieldAlert className="text-blue-500 w-5 h-5" />;
};

// 🎨 BORDER COLOR (INLINE — 100% WORKING)
const getBorderColor = (type: string) => {
  const t = type?.toLowerCase();

  if (t === "fire") return "#ef4444";     // red
  if (t === "medical") return "#22c55e";  // green
  if (t === "security") return "#3b82f6"; // blue

  return "#d1d5db"; // gray fallback
};

const EmergencyCard = ({
  alert,
  onResolve,
}: {
  alert: Alert;
  onResolve: (id: string) => void;
}) => {
  return (
    <div
      style={{ borderLeft: `4px solid ${getBorderColor(alert.type)}` }}
      className="bg-white p-5 rounded-2xl shadow-sm border border-gray-200 hover:shadow-lg hover:-translate-y-1 transition-all duration-300"
    >
      {/* HEADER */}
      <div className="flex justify-between items-start mb-3">
        
        <div className="flex items-center gap-2">
          {getIcon(alert.type)}
          <h3 className="text-lg font-semibold text-gray-800">
            {alert.type}
          </h3>
        </div>

        <span
          className={`px-3 py-1 rounded-full text-xs font-medium ${
            alert.status === "Active"
              ? "bg-yellow-100 text-yellow-700"
              : "bg-gray-200 text-gray-700"
          }`}
        >
          {alert.status}
        </span>
      </div>

      {/* MESSAGE */}
      <p className="text-gray-600 mb-2">
        {alert.message}
      </p>

      {/* TIME */}
      <p className="text-gray-400 text-xs mb-4">
        {new Date(alert.timestamp).toLocaleString()}
      </p>

      {/* BUTTON */}
      {alert.status === "Active" && (
        <button
          onClick={() => onResolve(alert.id)}
          className="bg-gradient-to-r from-blue-500 to-purple-500 text-white px-4 py-2 rounded-lg hover:scale-105 active:scale-95 transition-all duration-300"
        >
          Mark Resolved
        </button>
      )}
    </div>
  );
};

export default EmergencyCard;