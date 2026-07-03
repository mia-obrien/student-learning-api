from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


@router.post("", response_model=schemas.EnrollmentResponse, status_code=201)
def create_enrollment(enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    created_enrollment = crud.create_enrollment(db, enrollment)
    if created_enrollment is None:
        raise HTTPException(status_code=404, detail="Student or course not found")
    return created_enrollment


@router.get("", response_model=list[schemas.EnrollmentResponse])
def get_enrollments(db: Session = Depends(get_db)):
    return crud.get_enrollments(db)


@router.delete("/{enrollment_id}", response_model=schemas.EnrollmentResponse)
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    enrollment = crud.delete_enrollment(db, enrollment_id)
    if enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment