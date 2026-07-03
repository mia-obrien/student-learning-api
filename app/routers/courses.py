from fastapi import APIRouter

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

@router.get("/")
def get_courses():
    return [
        {
            "id": 101,
            "course": "Software Engineering",
            "credits": 3
        }
    ]