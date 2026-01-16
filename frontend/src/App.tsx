import { use, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [area, setArea] = useState(10);
  const [youngModulus, setYoungModulus] = useState(100);
  const [length, setLength] = useState(1000);
  const [k, setK] = useState([1, 2]);

  async function calculate_2() {

    const data = { "area": area, "elastic_modulus": youngModulus, "length": length };

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
    <h1>Structural Sala App</h1>
    <div class="main-app">
    <div class="sidebar">
      <p>App 1</p>
      <p>App 2</p>
      <p>App 3</p>
      <p>App 4</p>
      <p>App 5</p>
    </div>
    <div class="current-page">
      <table>
        <thead>
          <tr><td>id</td> <td> Area </td> <td> Young Modulus </td> <td> Length </td> <td> Stiffness </td></tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td><input type='number' placeholder='Area' value={area} onChange={e => setArea(Number(e.target.value))} /> </td>
            <td> <input type='number' placeholder='Young Modulus' value={youngModulus} onChange={e => setYoungModulus(Number(e.target.value))} /> </td>
            <td><input type='number' placeholder='Length' value={length} onChange={e => setLength(Number(e.target.value))} />
             </td>
             <td> {k} </td>
             <td>  <button onClick={calculate_2}>Submit!</button> </td>
          </tr>
        </tbody>
      </table>
      </div>
</div>
    </>
  )
}

export default App