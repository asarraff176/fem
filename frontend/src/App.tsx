import { use, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'





function App() {
  const [area, setArea] = useState(10);
  const [youngModulus, setYoungModulus] = useState(100);
  const [length, setLength] = useState(1000);
  const [k, setK] = useState([1, 2]);

  async function calculate() {
    const res = await fetch("http://localhost:8000/add?a=2&b=3")
    const data = await res.json()

    setK(data.result)
  }

  async function calculate_2() {

    const data = { "area": 2.0, "elastic_modulus": 3.0, "length": 4.0};

    const res = await fetch("http://localhost:8000/get_truss_local_stiffness_matrix", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    const result = await res.json();
    console.log(result.stiffness);
    setK(result.stiffness);
  }

  return (
    <>
      <input type='number' placeholder='Area' value={area} onChange={e => setArea(Number(e.target.value))} />
      <input type='number' placeholder='Young Modulus' value={youngModulus} onChange={e => setYoungModulus(Number(e.target.value))} />
      <input type='number' placeholder='Length' value={length} onChange={e => setLength(Number(e.target.value))} />
      <button onClick={calculate_2}>Submit!</button>
      <p>Stiffness: {k}</p>
    </>
  )
}

export default App