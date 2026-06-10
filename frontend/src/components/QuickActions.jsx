export default function QuickActions() {

  return (
    <div className="weather-card p-4">

      <h4 className="mb-4">
        Quick Actions
      </h4>

      <div className="row g-3">

        <div className="col-6">
          <button className="btn btn-success w-100">
            AI Chat
          </button>
        </div>

        <div className="col-6">
          <button className="btn btn-primary w-100">
            Weather
          </button>
        </div>

        <div className="col-6">
          <button className="btn btn-warning w-100">
            Reports
          </button>
        </div>

        <div className="col-6">
          <button className="btn btn-info w-100">
            Voice Query
          </button>
        </div>

      </div>

    </div>
  );
}