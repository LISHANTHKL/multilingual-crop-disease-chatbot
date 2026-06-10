import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const getProfile = async (email) => {

  const response = await axios.get(
    `${API_URL}/api/profile/${email}`
  );

  return response.data;
};