from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import Base

from app.routers import students, courses, enrollments

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Learning API",
    description="A REST API for managing students, courses, and enrollments.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1):517\d+",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students.router)
app.include_router(courses.router)
app.include_router(enrollments.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to the Student Learning API!"
    }