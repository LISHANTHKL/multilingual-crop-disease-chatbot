import axios from "axios";

const API =
  "http://localhost:8000/api/farmer-intelligence";

export const getFarmerRecommendations =
  async (userId) => {

    const response =
      await axios.get(
        `${API}/recommendations/${userId}`
      );

    return response.data;
  };