import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

export default function AnalyticsChart() {

  const data = [
    {
      day: "Mon",
      queries: 12
    },
    {
      day: "Tue",
      queries: 20
    },
    {
      day: "Wed",
      queries: 18
    },
    {
      day: "Thu",
      queries: 30
    },
    {
      day: "Fri",
      queries: 25
    }
  ];

  return (
    <div className="weather-card p-4 h-100">

      <h4 className="mb-4">
        Weekly Query Analytics
      </h4>

      <ResponsiveContainer
        width="100%"
        height={250}
      >

        <BarChart data={data}>

          <XAxis dataKey="day" />

          <YAxis />

          <Tooltip />

          <Bar
            dataKey="queries"
            fill="#16a34a"
          />

        </BarChart>

      </ResponsiveContainer>

    </div>
  );
}