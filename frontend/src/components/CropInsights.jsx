export default function CropInsights() {
  return (
    <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">

      <h2 className="text-xl font-bold mb-5">
        AI Crop Health Insights
      </h2>

      <div className="bg-green-500/20 border border-green-500 p-4 rounded-xl">

        <h3 className="font-bold text-green-400">
          Recommendation
        </h3>

        <p className="mt-2">
          Current humidity is high. Monitor crops for fungal diseases and inspect leaves every 3 days.
        </p>

      </div>

    </div>
  );
}