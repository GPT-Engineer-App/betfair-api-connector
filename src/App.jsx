import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Index from "./pages/Index.jsx";
import TestBetfairAPI from "./pages/TestBetfairAPI.jsx";

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Index />} />
      <Route path="/test-betfair" element={<TestBetfairAPI />} />
      </Routes>
    </Router>
  );
}

export default App;