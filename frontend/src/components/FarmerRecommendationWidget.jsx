import {
  useEffect,
  useState
} from "react";

import {
  getFarmerRecommendations
} from "../services/farmerIntelligenceService";

export default function FarmerRecommendationWidget() {

  const [data, setData] =
    useState(null);

  useEffect(() => {

    loadData();

  }, []);

  const loadData =
    async () => {

      try {

        const response =
          await getFarmerRecommendations(
            "farmer001"
          );

        setData(
          response
        );

      } catch (error) {

        console.error(error);

      }
    };

  if (!data) {

    return (
      <div>
        Loading...
      </div>
    );
  }

  return (

    <div className="card shadow-lg border-0">

      <div className="card-header bg-warning">

        🌱 Personalized Farmer Recommendations

      </div>

      <div className="card-body">

        {
          data.recommendations.map(
            (
              item,
              index
            ) => (

              <div
                key={index}
                className="mb-2"
              >
                ✅ {item}
              </div>

            )
          )
        }

      </div>

    </div>

  );
}