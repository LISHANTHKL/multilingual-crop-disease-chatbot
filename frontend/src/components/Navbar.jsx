export default function Navbar() {
  return (
    <header className="h-20 bg-slate-900 border-b border-slate-800 flex justify-between items-center px-8">

      <div>

        <h2 className="text-3xl font-bold">
          Welcome Back 👋
        </h2>

        <p className="text-slate-400">
          Multilingual Crop Disease Knowledge Chatbot
        </p>

      </div>

      <div className="bg-green-500 text-black px-5 py-2 rounded-xl font-semibold">
        Farmer
      </div>

    </header>
  );
}