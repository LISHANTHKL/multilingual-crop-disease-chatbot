export default function HeroBanner() {
  return (
    <div className="rounded-3xl bg-gradient-to-r from-green-500 via-emerald-600 to-cyan-600 p-8 shadow-2xl">

      <h1 className="text-4xl font-bold">
        AI Agriculture Assistant 🌱
      </h1>

      <p className="mt-3 text-lg opacity-90">
        Multilingual Crop Disease Knowledge Chatbot
      </p>

      <div className="mt-6 flex gap-4">

        <button className="bg-white text-black px-6 py-3 rounded-xl font-semibold">
          Start AI Chat
        </button>

        <button className="bg-black/20 px-6 py-3 rounded-xl">
          View Reports
        </button>

      </div>
    </div>
  );
}