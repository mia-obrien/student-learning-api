from typing import Optional

from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    major: str


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    major: Optional[str] = None


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True


class CourseCreate(BaseModel):
    course_code: str
    course_name: str
    credits: int


class CourseUpdate(BaseModel):
    course_code: Optional[str] = None
    course_name: Optional[str] = None
    credits: Optional[int] = None


class CourseResponse(CourseCreate):
    id: int

    class Config:
        from_attributes = True


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int


class EnrollmentResponse(EnrollmentCreate):
    id: int

    class Config:
        from_attributes = True