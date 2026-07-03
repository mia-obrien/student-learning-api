def test_create_and_get_courses(client_and_db):
    client, SessionLocal = client_and_db

    payload = {
        "course_code": "CS101",
        "course_name": "Intro to Computer Science",
        "credits": 3,
    }

    create_response = client.post("/courses", json=payload)
    assert create_response.status_code == 201
    body = create_response.json()
    assert body["course_code"] == payload["course_code"]
    assert body["course_name"] == payload["course_name"]
    assert body["credits"] == payload["credits"]

    with SessionLocal() as db:
        course = __import__("app.models", fromlist=["Course"]).Course
        assert db.query(course).count() == 1

    get_response = client.get("/courses")
    assert get_response.status_code == 200
    courses = get_response.json()
    assert len(courses) == 1
    assert courses[0]["course_code"] == payload["course_code"]


def test_get_course_by_id(client_and_db):
    client, _ = client_and_db

    created = client.post(
        "/courses",
        json={"course_code": "MATH201", "course_name": "Calculus", "credits": 4},
    )
    course_id = created.json()["id"]

    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["id"] == course_id
    assert response.json()["course_name"] == "Calculus"


def test_update_course(client_and_db):
    client, _ = client_and_db

    created = client.post(
        "/courses",
        json={"course_code": "ENG101", "course_name": "English", "credits": 2},
    )
    course_id = created.json()["id"]

    response = client.put(f"/courses/{course_id}", json={"credits": 3})
    assert response.status_code == 200
    assert response.json()["credits"] == 3
    assert response.json()["course_code"] == "ENG101"


def test_delete_course(client_and_db):
    client, SessionLocal = client_and_db

    created = client.post(
        "/courses",
        json={"course_code": "BIO101", "course_name": "Biology", "credits": 3},
    )
    course_id = created.json()["id"]

    delete_response = client.delete(f"/courses/{course_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["id"] == course_id

    with SessionLocal() as db:
        course = __import__("app.models", fromlist=["Course"]).Course
        assert db.query(course).filter(course.id == course_id).first() is None


def test_course_not_found_returns_404(client_and_db):
    client, _ = client_and_db

    response = client.get("/courses/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Course not found"
