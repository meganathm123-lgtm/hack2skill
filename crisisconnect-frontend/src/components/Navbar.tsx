const Navbar = () => {
  

  const handleLogout = () => {
  localStorage.removeItem("token");
  window.location.href = "/login";
};

 

  return (
   <div className="bg-white/70 backdrop-blur-md shadow-sm border-b px-6 py-4 flex justify-between items-center sticky top-0 z-50">
      
      <h1 className="text-xl font-bold text-gray-800 tracking-wide">
  🚨 CrisisConnect AI
</h1>

      <button
        onClick={handleLogout}
        
        className="bg-red-500 px-4 py-2 rounded-xl text-white hover:bg-red-600 transition"
      >
        Logout
        
      </button>
    </div>
  );
};

export default Navbar;