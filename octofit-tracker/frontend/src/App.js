

import OctofitLogo from './components/OctofitLogo';


function App() {
  return (
    <Router>
      <nav className="navbar navbar-expand-lg navbar-dark bg-octofit shadow-sm">
        <div className="container-fluid">
          <Link className="navbar-brand d-flex align-items-center" to="/">
            <OctofitLogo height={40} />
            <span className="fw-bold ms-2" style={{ fontSize: '1.5rem', color: '#ffb347' }}>OctoFit Tracker</span>
          </Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item"><Link className="nav-link" to="/activities">Activities</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/leaderboard">Leaderboard</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/teams">Teams</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/users">Users</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/workouts">Workouts</Link></li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container mt-4">
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={
            <div className="card shadow">
              <div className="card-body">
                <h2 className="card-title text-primary mb-3">Welcome to OctoFit Tracker!</h2>
                <p className="card-text">Track your fitness activities, join teams, view leaderboards, and more. Use the navigation menu to get started.</p>
                <Link to="/activities" className="btn btn-primary me-2">View Activities</Link>
                <Link to="/leaderboard" className="btn btn-outline-info">View Leaderboard</Link>
              </div>
            </div>
          } />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
