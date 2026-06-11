import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  ResponsiveContainer,
  LineChart,
  Line,
  Legend
} from "recharts";

const COLORS = [
  "#22c55e",
  "#3b82f6",
  "#f59e0b",
  "#ef4444",
  "#8b5cf6",
  "#06b6d4",
  "#84cc16"
];

export default function AnalyticsDashboard({
  cropData,
  diseaseData,
  activityData
}) {

  return (

    <div className="row g-4">

      {/* Crop Distribution */}

      <div className="col-md-4">

        <div className="card shadow-lg border-0 bg-dark text-white analytics-card">

          <div className="card-header bg-success text-white fw-bold">
            🌾 Crop Distribution
          </div>

          <div className="card-body">

            <ResponsiveContainer
              width="100%"
              height={250}
            >

              <PieChart>

                <Pie
                  data={cropData}
                  dataKey="count"
                  nameKey="_id"
                  outerRadius={80}
                  label
                >

                  {
                    cropData.map(
                      (_, index) => (
                        <Cell
                          key={index}
                          fill={
                            COLORS[
                              index % COLORS.length
                            ]
                          }
                        />
                      )
                    )
                  }

                </Pie>

                <Tooltip />

                <Legend />

              </PieChart>

            </ResponsiveContainer>

          </div>

        </div>

      </div>

      {/* Disease Distribution */}

      <div className="col-md-4">

        <div className="card shadow-lg border-0 bg-dark text-white analytics-card">

          <div className="card-header bg-primary text-white fw-bold">
            🦠 Disease Distribution
          </div>

          <div className="card-body">

            <ResponsiveContainer
              width="100%"
              height={250}
            >

              <BarChart
                data={diseaseData}
              >

                <CartesianGrid strokeDasharray="3 3" />

                <XAxis
                  dataKey="_id"
                  tick={{
                    fill: "#ffffff"
                  }}
                />

                <YAxis
                  tick={{
                    fill: "#ffffff"
                  }}
                />

                <Tooltip />

                <Bar
                  dataKey="count"
                  fill="#22c55e"
                  radius={[8, 8, 0, 0]}
                />

              </BarChart>

            </ResponsiveContainer>

          </div>

        </div>

      </div>

      {/* Daily Activity */}

      <div className="col-md-4">

        <div className="card shadow-lg border-0 bg-dark text-white analytics-card">

          <div className="card-header bg-info text-white fw-bold">
            📈 Daily Activity
          </div>

          <div className="card-body">

            <ResponsiveContainer
              width="100%"
              height={250}
            >

              <LineChart
                data={activityData}
              >

                <CartesianGrid strokeDasharray="3 3" />

                <XAxis
                  dataKey="_id"
                  tick={{
                    fill: "#ffffff"
                  }}
                />

                <YAxis
                  tick={{
                    fill: "#ffffff"
                  }}
                />

                <Tooltip />

                <Line
                  type="monotone"
                  dataKey="count"
                  stroke="#3b82f6"
                  strokeWidth={3}
                  dot={{
                    r: 5
                  }}
                />

              </LineChart>

            </ResponsiveContainer>

          </div>

        </div>

      </div>

    </div>

  );
}
