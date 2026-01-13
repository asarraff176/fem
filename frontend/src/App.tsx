import { use, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

async function calculate(setK){
  const res = await fetch("http://localhost:8000/add?a=2&b=3")
  const data = await res.json()

  setK(Number(data.result))
}

function App() {
  const [area, setArea] = useState(10)
  const [youngModulus, setYoungModulus] = useState(100)
  const [length, setLength] = useState(1000)
  const [k, setK] = useState(0)
  return (
    <>
      <input type='number' placeholder='Area' value={area} onChange={e => setArea(Number(e.target.value))} />
      <input type='number' placeholder='Young Modulus' value={youngModulus} onChange={e => setYoungModulus(Number(e.target.value))} />
      <input type='number' placeholder='Length' value={length} onChange={e => setLength(Number(e.target.value))} />
      <button onClick={e => calculate(setK)}>Submit!</button>
      <p>Stiffness: {k}</p>
    </>
  )
}

export default App