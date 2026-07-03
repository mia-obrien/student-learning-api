# Student Learning System

A full-stack student management application built with FastAPI, SQLite, React, and Vite. The project allows users to add and view students through a simple web interface while persisting data in a SQLite database.

## Features

- FastAPI backend with REST endpoints for students
- SQLite database persistence
- React + Vite frontend with Axios for API communication
- Simple form-based student creation flow
- Responsive, lightweight UI for portfolio use

## Project Structure

- `app/` - FastAPI backend, database config, models, CRUD, and routers
- `frontend/` - React + Vite frontend
- `tests/` - Backend test files
- `student_learning.db` - SQLite database file

## Tech Stack

- Backend: FastAPI, SQLAlchemy, SQLite
- Frontend: React, Vite, Axios
- Python version: 3.10+
- Node.js version: 18+

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd student-learning-api
```

### 2. Set up the backend

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run the backend:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- http://127.0.0.1:8000
- API docs: http://127.0.0.1:8000/docs

### 3. Set up the frontend

Open a new terminal and navigate to the frontend folder:

```bash
cd frontend
npm install
npm run dev
```

The React app will be available at:

- http://127.0.0.1:5173

## API Endpoints

### Students

- `GET /students` - Retrieve all students
- `POST /students` - Create a new student
- `GET /students/{id}` - Retrieve one student
- `PUT /students/{id}` - Update a student
- `DELETE /students/{id}` - Delete a student

## Example Student Payload

```json
{
  "first_name": "Ada",
  "last_name": "Lovelace",
  "email": "ada@example.com",
  "major": "Computer Science"
}
```

## Notes

- The SQLite database is created automatically when the backend starts.
- The frontend communicates with the backend through Axios using the base URL `http://127.0.0.1:8000`.
