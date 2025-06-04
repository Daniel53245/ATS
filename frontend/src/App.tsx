import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [message, setMessage] = useState("Loading...")

  useEffect(() => {
    axios.get("http://localhost:8000/api/hello")
      .then(response => setMessage(response.data.msg))
      .catch(() => setMessage("Failed to connect to backend"))
  }, [])

  return (
    <div className="min-h-screen flex items-center justify-center text-xl font-semibold">
      <p>{message}</p>
    </div>
  )
}

export default App
