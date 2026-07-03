from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post("", response_model=schemas.CourseResponse, status_code=201)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)


@router.get("", response_model=list[schemas.CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    return crud.get_courses(db)


@router.get("/{course_id}", response_model=schemas.CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = crud.get_course_by_id(db, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.put("/{course_id}", response_model=schemas.CourseResponse)
def update_course(course_id: int, course_update: schemas.CourseUpdate, db: Session = Depends(get_db)):
    course = crud.update_course(db, course_id, course_update)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.delete("/{course_id}", response_model=schemas.CourseResponse)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course = crud.delete_course(db, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course