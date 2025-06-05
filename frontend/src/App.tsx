import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [message, setMessage] = useState("Loading...")
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    // When running in Docker, use the service name
    // When accessed from browser, use localhost
    const apiUrl = "/api"
    console.log('Attempting to connect to:', apiUrl);
    
    axios.get(`${apiUrl}/test-user`, {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      withCredentials: true,
      timeout: 5000
    })
      .then(response => {
        console.log('Response:', response.data);
        setMessage(response.data.msg);
        setError(null);
      })
      .catch((error) => {
        console.error('Error connecting to backend:', error);
        if (error.response) {
          // The request was made and the server responded with a status code
          // that falls out of the range of 2xx
          console.error('Response data:', error.response.data);
          console.error('Response status:', error.response.status);
          console.error('Response headers:', error.response.headers);
        } else if (error.request) {
          // The request was made but no response was received
          console.error('No response received:', error.request);
        } else {
          // Something happened in setting up the request that triggered an Error
          console.error('Error message:', error.message);
        }
        setError(error.message);
        setMessage("Failed to connect to backend");
      });
  }, [])

  return (
    <div className="min-h-screen flex flex-col items-center justify-center text-xl font-semibold">
      
      <p>The messgae:{message}</p>
      {error && (
        <p className="text-red-500 text-sm mt-2">
          Error: {error}
        </p>
      )}
    </div>
  )
}

export default App
