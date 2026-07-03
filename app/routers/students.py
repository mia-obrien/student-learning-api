from fastapi import APIRouter

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.get("/")
def get_students():
    return [
        {
            "id": 1,
            "name": "Alice Johnson",
            "major": "Computer Science"
        }
    ]