import { useNavigate } from "react-router-dom";

export default function Sidebar() {

  const navigate = useNavigate();

  const logout = () => {

    localStorage.removeItem("token");
    localStorage.removeItem("userEmail");

    navigate("/login");

  };

  return (
    <div className="sidebar d-flex flex-column">

      <div className="p-4">

        <h2 className="text-success fw-bold">
          AgroAI
        </h2>

        <p className="text-secondary">
          Smart Farming Assistant
        </p>

      </div>

      <div className="px-3">

        <button
          className="btn btn-success w-100 text-start mb-2"
          onClick={() => navigate("/")}
        >
          <i className="bi bi-house me-2"></i>
          Dashboard
        </button>

        <button
          className="btn btn-dark w-100 text-start mb-2"
          onClick={() => navigate("/chatbot")}
        >
          <i className="bi bi-robot me-2"></i>
          AI Assistant
        </button>

        <button
          className="btn btn-dark w-100 text-start mb-2"
          onClick={() => navigate("/weather")}
        >
          <i className="bi bi-cloud-sun me-2"></i>
          Weather
        </button>

        <button
          className="btn btn-dark w-100 text-start mb-2"
          onClick={() => navigate("/reports")}
        >
          <i className="bi bi-file-earmark-text me-2"></i>
          Reports
        </button>

        <button
          className="btn btn-dark w-100 text-start mb-2"
          onClick={() => navigate("/profile")}
        >
          <i className="bi bi-person me-2"></i>
          Profile
        </button>

      </div>

      <div className="mt-auto p-3">

        <button
          className="btn btn-danger w-100"
          onClick={logout}
        >
          <i className="bi bi-box-arrow-right me-2"></i>
          Logout
        </button>

      </div>

    </div>
  );
}

