import { useState } from 'react'
import api from '../api'

function AddStudent({ onStudentAdded }) {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    major: '',
  })
  const [message, setMessage] = useState('')
  const [error, setError] = useState('')

  const handleChange = (event) => {
    const { name, value } = event.target
    setFormData((current) => ({ ...current, [name]: value }))
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    setMessage('')
    setError('')

    try {
      await api.post('/students', formData)
      setMessage('Student added successfully!')
      setFormData({ first_name: '', last_name: '', email: '', major: '' })
      onStudentAdded()
    } catch (err) {
      setError('Unable to add student. Please check the form values.')
    }
  }

  return (
    <section className="card">
      <h2>Add Student</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-grid">
          <label>
            First Name
            <input name="first_name" value={formData.first_name} onChange={handleChange} required />
          </label>
          <label>
            Last Name
            <input name="last_name" value={formData.last_name} onChange={handleChange} required />
          </label>
          <label>
            Email
            <input type="email" name="email" value={formData.email} onChange={handleChange} required />
          </label>
          <label>
            Major
            <input name="major" value={formData.major} onChange={handleChange} required />
          </label>
        </div>
        <button type="submit">Add Student</button>
      </form>
      {message && <p className="message success">{message}</p>}
      {error && <p className="message error">{error}</p>}
    </section>
  )
}

export default AddStudent
