import React, { useEffect, useState } from 'react';
import Box from '@mui/material/Box';
import { TextField } from '@mui/material/TextField';

const Scholarships = () => {
  const [scholarships, setScholarships] = useState([]);

  useEffect(() => {
    async function fetchData() {

    const response = await fetch('http://127.0.0.1:5000/all_scholarships');
    const data = await response.json();
    setScholarships(data);
    }
    fetchData();
    }, []);
console.log(scholarships);

  return (
    <div>
      <h1>Scholarships</h1>
        <h2>Available Scholarships</h2>
        {scholarships.map((scholarship) => (
            <li key={scholarship.id}>
            <h3>{scholarship.name}</h3>
            <p>{scholarship.description}</p>
            <p>{scholarship.value}</p>
          </li>
        ))}
      <ul>

      </ul>
    </div>
  );
};

export default Scholarships;
