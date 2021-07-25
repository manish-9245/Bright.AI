import {
  BrowserRouter as Router,
  Route,
} from "react-router-dom";
import SearchDoctors from './pages/SearchDoctors';  
import Navbar from "./components/Navbar";
import DoctorProfile from "./pages/DoctorProfile";


function App() {
  return (
    <div>
      <Navbar />
    <Router>
    <Route exact path="/" component={SearchDoctors} />
    <Route exact path="/doctor/:id" component={DoctorProfile} />
    </Router>
    </div>
  );
}

export default App;
