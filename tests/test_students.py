import pytest


def test_create_and_get_students(client_and_db):
    client, SessionLocal = client_and_db

    payload = {
        "first_name": "Alice",
        "last_name": "Johnson",
        "email": "alice@example.com",
        "major": "Computer Science",
    }

    create_response = client.post("/students", json=payload)
    assert create_response.status_code == 201
    body = create_response.json()
    assert body["first_name"] == payload["first_name"]
    assert body["last_name"] == payload["last_name"]
    assert body["email"] == payload["email"]
    assert body["major"] == payload["major"]
    assert body["id"] is not None

    with SessionLocal() as db:
        student_count = db.query(__import__("app.models", fromlist=["Student"]).Student).count()
        assert student_count == 1

    get_response = client.get("/students")
    assert get_response.status_code == 200
    students = get_response.json()
    assert len(students) == 1
    assert students[0]["email"] == payload["email"]


def test_get_student_by_id(client_and_db):
    client, _ = client_and_db

    create_response = client.post(
        "/students",
        json={
            "first_name": "Bob",
            "last_name": "Smith",
            "email": "bob@example.com",
            "major": "Mathematics",
        },
    )
    student_id = create_response.json()["id"]

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["id"] == student_id
    assert response.json()["first_name"] == "Bob"


def test_update_student(client_and_db):
    client, _ = client_and_db

    created = client.post(
        "/students",
        json={
            "first_name": "Carol",
            "last_name": "Brown",
            "email": "carol@example.com",
            "major": "History",
        },
    )
    student_id = created.json()["id"]

    update_response = client.put(
        f"/students/{student_id}",
        json={"major": "Physics"},
    )
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["major"] == "Physics"
    assert data["first_name"] == "Carol"


def test_delete_student(client_and_db):
    client, SessionLocal = client_and_db

    created = client.post(
        "/students",
        json={
            "first_name": "Diana",
            "last_name": "Prince",
            "email": "diana@example.com",
            "major": "Engineering",
        },
    )
    student_id = created.json()["id"]

    delete_response = client.delete(f"/students/{student_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["id"] == student_id

    with SessionLocal() as db:
        student = __import__("app.models", fromlist=["Student"]).Student
        assert db.query(student).filter(student.id == student_id).first() is None


def test_student_not_found_returns_404(client_and_db):
    client, _ = client_and_db

    response = client.get("/students/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"
