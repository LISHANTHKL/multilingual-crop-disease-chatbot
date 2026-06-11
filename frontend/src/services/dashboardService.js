import axios from "axios";

const API =
  "http://localhost:8000/api/dashboard";

export const getDashboardStats =
  async () => {

    const response =
      await axios.get(
        `${API}/stats`
      );

    return response.data;
  };

export const getRecentConversations =
  async () => {

    const response =
      await axios.get(
        `${API}/recent-conversations`
      );

    return response.data;
  };

