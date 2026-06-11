import {
  useEffect,
  useState
} from "react";

import {
  getInsights
} from "../services/intelligenceService";

export default function IntelligenceWidget() {

  const [insights,
    setInsights] = useState([]);

  useEffect(() => {

    loadInsights();

  }, []);

  const loadInsights =
    async () => {

      try {

        const data =
          await getInsights();

        setInsights(
          data.insights
        );

      } catch (error) {

        console.error(error);

      }
    };

  return (

    <div className="card shadow-lg border-0">

      <div className="card-header bg-success text-white">

        🌾 Agriculture Intelligence

      </div>

      <div className="card-body">

        {
          insights.map(
            (
              item,
              index
            ) => (

              <div
                key={index}
                className="mb-3"
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