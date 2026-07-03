import { useEffect, useState } from 'react'
import api from '../api'

function StudentList({ refreshKey }) {
  const [students, setStudents] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const fetchStudents = async () => {
      try {
        setLoading(true)
        const response = await api.get('/students')
        setStudents(response.data)
        setError('')
      } catch (err) {
        setError('Unable to load students right now.')
      } finally {
        setLoading(false)
      }
    }

    fetchStudents()
  }, [refreshKey])

  return (
    <section className="card">
      <h2>Students</h2>
      {loading && <p>Loading students...</p>}
      {error && <p className="message error">{error}</p>}
      {!loading && !error && students.length === 0 && <p>No students yet.</p>}
      {!loading && !error && students.length > 0 && (
        <table className="student-table">
          <thead>
            <tr>
              <th>First Name</th>
              <th>Last Name</th>
              <th>Email</th>
              <th>Major</th>
            </tr>
          </thead>
          <tbody>
            {students.map((student) => (
              <tr key={student.id}>
                <td>{student.first_name}</td>
                <td>{student.last_name}</td>
                <td>{student.email}</td>
                <td>{student.major}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </section>
  )
}

export default StudentList
