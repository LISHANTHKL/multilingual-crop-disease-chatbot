export default function StatsCard({
  title,
  value,
  color,
}) {
  return (
    <div
      className={`rounded-3xl p-6 backdrop-blur-xl border border-white/10 ${color}`}
    >
      <p className="text-slate-300">
        {title}
      </p>

      <h2 className="text-4xl font-bold mt-4">
        {value}
      </h2>
    </div>
  );
}