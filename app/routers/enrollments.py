from fastapi import APIRouter

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)

@router.get("/")
def get_enrollments():
    return [
        {
            "student": "Alice Johnson",
            "course": "Software Engineering"
        }
    ]