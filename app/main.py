from fastapi import FastAPI
from app.routers import students, courses, enrollments

app = FastAPI(
    title="Student Learning API",
    description="A REST API for managing students, courses, and enrollments.",
    version="1.0.0"
)

app.include_router(students.router)
app.include_router(courses.router)
app.include_router(enrollments.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to the Student Learning API!"
    }
