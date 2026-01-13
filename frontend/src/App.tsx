import { use, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <div>
//         <a href="https://vite.dev" target="_blank">
//           <img src={viteLogo} className="logo" alt="Vite logo" />
//         </a>
//         <a href="https://react.dev" target="_blank">
//           <img src={reactLogo} className="logo react" alt="React logo" />
//         </a>
//       </div>
//       <h1>Vite + React</h1>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 1)}>
//           count is {count}
//         </button>
//         <p>
//           Edit <code>src/App.tsx</code> and save to test HMR
//         </p>
//       </div>
//       <p className="read-the-docs">
//         Click on the Vite and React logos to learn more
//       </p>
//     </>
//   )
// }

function InputField( {label, value, onChange}) {
  
  return(
    <tr>
      <td>{label}</td>
      <td><input name="name" type="text" onChange={onChange} /></td>
    </tr>)
  }


function MyButton( {label, count, onClick}) {

  return <>
  <button onClick={onClick}> {label} </button></>
}

function App() {

  const [a, setA] = useState("")
  const [b, setB] = useState("")
  const [result, setResult] = useState<number | null>(null)

  async function calculate() {
    const res = await fetch("localhost:8000/add", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        a: Number(a),
        b: Number(b),
      }),
    })

    const data = await res.json()
    setResult(data.result)
  }

  
  return (
    <div>
      <input
        type="number"
        value={a}
        onChange={e => setA(e.target.value)}
        placeholder="a"
      />

      <input
        type="number"
        value={b}
        onChange={e => setB(e.target.value)}
        placeholder="b"
      />

      <button onClick={calculate}>Add</button>

      {result !== null && <p>Result: {result}</p>}
    </div>
  )
}


export default App
