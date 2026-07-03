def test_create_and_get_enrollments(client_and_db):
    client, SessionLocal = client_and_db

    student_response = client.post(
        "/students",
        json={
            "first_name": "Eve",
            "last_name": "Adams",
            "email": "eve@example.com",
            "major": "Chemistry",
        },
    )
    course_response = client.post(
        "/courses",
        json={"course_code": "CHEM101", "course_name": "General Chemistry", "credits": 3},
    )

    enrollment_response = client.post(
        "/enrollments",
        json={
            "student_id": student_response.json()["id"],
            "course_id": course_response.json()["id"],
        },
    )
    assert enrollment_response.status_code == 201
    body = enrollment_response.json()
    assert body["student_id"] == student_response.json()["id"]
    assert body["course_id"] == course_response.json()["id"]

    with SessionLocal() as db:
        enrollment = __import__("app.models", fromlist=["Enrollment"]).Enrollment
        assert db.query(enrollment).count() == 1

    get_response = client.get("/enrollments")
    assert get_response.status_code == 200
    enrollments = get_response.json()
    assert len(enrollments) == 1


def test_delete_enrollment(client_and_db):
    client, SessionLocal = client_and_db

    student_id = client.post(
        "/students",
        json={
            "first_name": "Frank",
            "last_name": "Castle",
            "email": "frank@example.com",
            "major": "Biology",
        },
    ).json()["id"]
    course_id = client.post(
        "/courses",
        json={"course_code": "BIO202", "course_name": "Advanced Biology", "credits": 4},
    ).json()["id"]
    enrollment_id = client.post(
        "/enrollments",
        json={"student_id": student_id, "course_id": course_id},
    ).json()["id"]

    delete_response = client.delete(f"/enrollments/{enrollment_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["id"] == enrollment_id

    with SessionLocal() as db:
        enrollment = __import__("app.models", fromlist=["Enrollment"]).Enrollment
        assert db.query(enrollment).filter(enrollment.id == enrollment_id).first() is None


def test_enrollment_requires_valid_student_and_course(client_and_db):
    client, _ = client_and_db

    invalid_student = client.post(
        "/enrollments",
        json={"student_id": 999, "course_id": 1},
    )
    assert invalid_student.status_code == 404
    assert invalid_student.json()["detail"] == "Student or course not found"

    invalid_course = client.post(
        "/enrollments",
        json={"student_id": 1, "course_id": 999},
    )
    assert invalid_course.status_code == 404
    assert invalid_course.json()["detail"] == "Student or course not found"
