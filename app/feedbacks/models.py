from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class GenericUser(AbstractUser):
    pass


class Student(GenericUser):
    LEVEL_3 = 3
    LEVEL_4 = 4
    LEVEL_5 = 5
    LEVEL_6 = 6

    LEVELS = (
        (LEVEL_3, "LEVEL 3"),
        (LEVEL_4, "LEVEL 4"),
        (LEVEL_5, "LEVEL 5"),
        (LEVEL_6, "LEVEL 6"),
    )

    MALE = 0
    FEMALE = 1

    GENDERS = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )

    guid = models.UUIDField(unique=True, default=uuid.uuid4)
    level = models.PositiveSmallIntegerField(choices=LEVELS, default=LEVEL_3)
    gender = models.PositiveSmallIntegerField(choices=GENDERS, null=True)
    is_scholarship = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Module(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=250, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


class Teacher(GenericUser):
    guid = models.UUIDField(unique=True, default=uuid.uuid4)
    module = models.ForeignKey(Module, related_name="teachers", on_delete=models.DO_NOTHING, null=True)
    is_leader = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Feedback(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    text = models.TextField()
    module = models.ForeignKey(Module, null=True, blank=True, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"Feedback from {self.student} for {self.module}{self.teacher}"
