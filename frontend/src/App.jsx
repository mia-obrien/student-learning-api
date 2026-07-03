import { useState } from 'react'
import AddStudent from './components/AddStudent'
import StudentList from './components/StudentList'
import './App.css'

function App() {
  const [refreshKey, setRefreshKey] = useState(0)

  const handleStudentAdded = () => {
    setRefreshKey((value) => value + 1)
  }

  return (
    <div className="app-shell">
      <header className="app-header">
        <h1>Student Learning System</h1>
        <p>Add and view students from the FastAPI backend.</p>
      </header>

      <main className="dashboard">
        <AddStudent onStudentAdded={handleStudentAdded} />
        <StudentList refreshKey={refreshKey} />
      </main>
    </div>
  )
}

export default App
