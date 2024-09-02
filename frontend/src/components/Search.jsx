import React, {useState, useEffect} from "react";

const Search = ({fetchScholarships }) => {
    const [scholarships, setScholarships] = useState([]);
    const [loading, setLoading] = useState(true);
    const [name, setName] = useState('');
    const [citizenship, setCitizenship] = useState('');
    const [minValue, setMinValue] = useState('');
    const [maxValue, setMaxValue] = useState('');
    const [university, setUniversity] = useState('');
    const [type, setType] = useState('');
    
    useEffect(() => {
        async function fetchData() {
            try {
                const response = await fetch('http://127.0.0.1:5000/all_scholarships');
                const data = await response.json();
                setScholarships(data); // Assuming the response is the array of scholarships
                setLoading(false);     // Data has been loaded
            } catch (error) {
                console.error("Error fetching scholarships:", error);
                setLoading(false);     // Ensure loading state is turned off even if there's an error
            }
        }
    
        fetchData();
    }, [fetchScholarships]); 
    const filterScholarships = () => {
        console.log(scholarships);
        return scholarships.filter(scholarship => {
            const matchesName = name === '' || scholarship.name.toLowerCase().includes(name.toLowerCase());
            const matchesCitizenship = citizenship === '' || scholarship.citizenship === citizenship;
            const matchesValue = (
                (minValue === '' || scholarship.value >= parseInt(minValue)) &&
                (maxValue === '' || scholarship.value <= parseInt(maxValue))
            );
            const matchesUniversity = university === '' || scholarship.university === university;
            const matchesType = type === '' || scholarship.type === type;

            return matchesName && matchesCitizenship && matchesValue && matchesUniversity && matchesType;
        });
    };

    if (loading) {
        return <div>Loading scholarships...</div>; // Loading state
    }

    return (
        <div>
            <h2>Search Scholarships</h2>
            <div>
                <input
                    type="text"
                    placeholder="Scholarship Name"
                    value={name}
                    onChange={e => setName(e.target.value)}
                />
            </div>
            <div>
                <select value={citizenship} onChange={e => setCitizenship(e.target.value)}>
                    <option value="">Select Citizenship Type</option>
                    <option value="domestic">Domestic</option>
                    <option value="international">International</option>
                </select>
            </div>
            <div>
                <input
                    type="number"
                    placeholder="Min Value"
                    value={minValue}
                    onChange={e => setMinValue(e.target.value)}
                />
                <input
                    type="number"
                    placeholder="Max Value"
                    value={maxValue}
                    onChange={e => setMaxValue(e.target.value)}
                />
            </div>
            <div>
                <input
                    type="text"
                    placeholder="University"
                    value={university}
                    onChange={e => setUniversity(e.target.value)}
                />
            </div>
            <div>
                <select value={type} onChange={e => setType(e.target.value)}>
                    <option value="">Select Type</option>
                    <option value="in-course">In-Course</option>
                    <option value="graduating">Graduating</option>
                    <option value="admission">Admission</option>
                </select>
            </div>
            <div>
                <button onClick={filterScholarships}>Search</button>
            </div>
            <div>
                <h3>Results</h3>
                <ul>
                    {filterScholarships().map(scholarship => (
                        <li key={scholarship.id}>
                            {scholarship.name} - {scholarship.university} - ${scholarship.value}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Search;