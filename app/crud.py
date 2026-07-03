from typing import Any

from sqlalchemy.orm import Session

from app import models


def _extract_data(data: Any, *, exclude_unset: bool = False) -> dict[str, Any]:
    if hasattr(data, "model_dump"):
        return data.model_dump(exclude_unset=exclude_unset)
    return data.dict(exclude_unset=exclude_unset)


def create_student(db: Session, student) -> models.Student:
    student_data = _extract_data(student)
    db_student = models.Student(**student_data)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_students(db: Session) -> list[models.Student]:
    return db.query(models.Student).all()


def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def update_student(db: Session, student_id: int, updated_data) -> models.Student | None:
    student = get_student_by_id(db, student_id)
    if student is None:
        return None

    data = _extract_data(updated_data, exclude_unset=True)
    for key, value in data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student


def delete_student(db: Session, student_id: int):
    student = get_student_by_id(db, student_id)
    if student is None:
        return None

    db.delete(student)
    db.commit()
    return student


def create_course(db: Session, course) -> models.Course:
    course_data = _extract_data(course)
    db_course = models.Course(**course_data)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def get_courses(db: Session) -> list[models.Course]:
    return db.query(models.Course).all()


def get_course_by_id(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


def update_course(db: Session, course_id: int, updated_data) -> models.Course | None:
    course = get_course_by_id(db, course_id)
    if course is None:
        return None

    data = _extract_data(updated_data, exclude_unset=True)
    for key, value in data.items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)
    return course


def delete_course(db: Session, course_id: int):
    course = get_course_by_id(db, course_id)
    if course is None:
        return None

    db.delete(course)
    db.commit()
    return course


def create_enrollment(db: Session, enrollment) -> models.Enrollment | None:
    enrollment_data = _extract_data(enrollment)

    student = get_student_by_id(db, enrollment_data.get("student_id"))
    course = get_course_by_id(db, enrollment_data.get("course_id"))
    if student is None or course is None:
        return None

    db_enrollment = models.Enrollment(**enrollment_data)
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment


def get_enrollments(db: Session) -> list[models.Enrollment]:
    return db.query(models.Enrollment).all()


def delete_enrollment(db: Session, enrollment_id: int):
    enrollment = db.query(models.Enrollment).filter(models.Enrollment.id == enrollment_id).first()
    if enrollment is None:
        return None

    db.delete(enrollment)
    db.commit()
    return enrollment
