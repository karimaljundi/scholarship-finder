import logo from './logo.svg';
import './App.css';
import Search from './components/Search';
const fetchScholarships = async () => {
  const response = await fetch('http://127.0.0.1:5000/all_scholarships');
  const data = await response.json();
  console.log(data[0]);
  return data; // Adjust this line based on your actual data structure
};

const App = () => {
  console.log(fetchScholarships());
  return (
      <div>
          <Search fetchScholarships={fetchScholarships} />
      </div>
  );
};

export default App;