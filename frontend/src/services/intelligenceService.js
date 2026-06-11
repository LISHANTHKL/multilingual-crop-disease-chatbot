import axios from "axios";

const API =
  "http://localhost:8000/api/intelligence";


export const getInsights =
  async () => {

    const response =
      await axios.get(
        `${API}/insights`
      );

    return response.data;
  };