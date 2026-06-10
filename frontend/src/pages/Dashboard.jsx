import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";

import AnalyticsChart from "../components/AnalyticsChart";
import UserProfileCard from "../components/UserProfileCard";
import RecentConversations from "../components/RecentConversations";
import QuickActions from "../components/QuickActions";

import { getDashboardStats } from "../services/dashboardService";

export default function Dashboard() {

  const [stats, setStats] = useState({
    totalUsers: 0,
    totalChats: 0,
    totalReports: 0,
    totalPredictions: 0,
  });

  useEffect(() => {

    const loadStats = async () => {

      try {

        const data = await getDashboardStats();

        setStats(data);

      } catch (error) {

        console.error(error);

      }

    };

    loadStats();

  }, []);

  return (
    <div className="d-flex">

      <Sidebar />

      <div className="main-content">

        <div className="container-fluid p-4">

          <div className="hero-card mb-4">

            <h1 className="fw-bold">
              Welcome Back 👋
            </h1>

            <h4>
              Multilingual Crop Disease Knowledge Chatbot
            </h4>

            <p className="mt-3">
              AI-powered Agriculture Assistant for Farmers
            </p>

          </div>

          {/* Stats */}

          <div className="row g-4 mb-4">

            <div className="col-md-3">
              <div className="stat-card">
                <h6>Total Users</h6>
                <h2>{stats.totalUsers}</h2>
              </div>
            </div>

            <div className="col-md-3">
              <div className="stat-card">
                <h6>Total Chats</h6>
                <h2>{stats.totalChats}</h2>
              </div>
            </div>

            <div className="col-md-3">
              <div className="stat-card">
                <h6>Total Reports</h6>
                <h2>{stats.totalReports}</h2>
              </div>
            </div>

            <div className="col-md-3">
              <div className="stat-card">
                <h6>Disease Predictions</h6>
                <h2>{stats.totalPredictions}</h2>
              </div>
            </div>

          </div>

          {/* Existing Widgets */}

          <div className="row g-4 mb-4">

            <div className="col-md-6">
              <AnalyticsChart />
            </div>

            <div className="col-md-6">
              <UserProfileCard />
            </div>

          </div>

          <div className="row g-4">

            <div className="col-md-6">
              <RecentConversations />
            </div>

            <div className="col-md-6">
              <QuickActions />
            </div>

          </div>

        </div>

      </div>

    </div>
  );
}