import pytest
from feedbacks.models import Student


@pytest.mark.django_db
def test_student_model():
    student = Student(email="f@gmail.com", password="12345678")
    student.save()

    assert student.email == "f@gmail.com"
    assert not student.is_staff

