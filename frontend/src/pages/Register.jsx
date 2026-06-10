import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import axios from "axios";

export default function Register() {

  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    password: "",
    state: "",
    preferred_language: "English"
  });

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });

  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    try {

      await axios.post(
        "http://127.0.0.1:8000/api/auth/register",
        formData
      );

      alert("Registration Successful");

      navigate("/login");

    } catch (error) {

      alert(
        error?.response?.data?.detail ||
        "Registration Failed"
      );

    }

  };

  return (
    <div
      className="d-flex justify-content-center align-items-center"
      style={{
        minHeight: "100vh",
        background: "#0f172a"
      }}
    >

      <div
        className="card p-4"
        style={{
          width: "500px",
          background: "#111827",
          color: "white",
          borderRadius: "20px"
        }}
      >

        <h2 className="text-success text-center mb-4">
          Farmer Registration
        </h2>

        <form onSubmit={handleSubmit}>

          <div className="mb-3">

            <label>Full Name</label>

            <input
              type="text"
              name="full_name"
              className="form-control"
              onChange={handleChange}
              required
            />

          </div>

          <div className="mb-3">

            <label>Email</label>

            <input
              type="email"
              name="email"
              className="form-control"
              onChange={handleChange}
              required
            />

          </div>

          <div className="mb-3">

            <label>Password</label>

            <input
              type="password"
              name="password"
              className="form-control"
              onChange={handleChange}
              required
            />

          </div>

          <div className="mb-3">

            <label>State</label>

            <input
              type="text"
              name="state"
              className="form-control"
              onChange={handleChange}
            />

          </div>

          <div className="mb-3">

            <label>Preferred Language</label>

            <select
              name="preferred_language"
              className="form-control"
              onChange={handleChange}
            >
              <option>English</option>
              <option>Hindi</option>
              <option>Kannada</option>
            </select>

          </div>

          <button
            type="submit"
            className="btn btn-success w-100"
          >
            Register
          </button>

        </form>

        <p className="mt-3 text-center">

          Already have an account?

          <Link
            to="/login"
            className="ms-2"
          >
            Login
          </Link>

        </p>

      </div>

    </div>
  );
}
