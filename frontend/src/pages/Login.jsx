import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import axios from "axios";

export default function Login() {

  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });

  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    try {

      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/api/auth/login",
        formData
      );

      localStorage.setItem(
        "token",
        response.data.access_token
      );

      localStorage.setItem(
        "userEmail",
        formData.email
      );

      alert("Login Successful");

      navigate("/");

    } catch (error) {

      alert(
        error?.response?.data?.detail ||
        "Login Failed"
      );

    } finally {

      setLoading(false);

    }

  };

  return (
    <div
      className="d-flex justify-content-center align-items-center"
      style={{
        minHeight: "100vh",
        background: "#0f172a",
      }}
    >

      <div
        className="card p-4"
        style={{
          width: "450px",
          background: "#111827",
          color: "white",
          borderRadius: "20px",
        }}
      >

        <h2 className="text-center mb-4 text-success">
          AgroAI Login
        </h2>

        <form onSubmit={handleSubmit}>

          <div className="mb-3">

            <label>Email</label>

            <input
              type="email"
              className="form-control"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
            />

          </div>

          <div className="mb-3">

            <label>Password</label>

            <input
              type="password"
              className="form-control"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
            />

          </div>

          <button
            type="submit"
            className="btn btn-success w-100"
          >

            {
              loading
                ? "Logging In..."
                : "Login"
            }

          </button>

        </form>

        <p className="text-center mt-3">

          Don't have an account?

          <Link
            to="/register"
            className="ms-2"
          >
            Register
          </Link>

        </p>

      </div>

    </div>
  );
}

