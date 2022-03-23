from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import uuid


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class GenericUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


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


class Teacher(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
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
    text = models.TextField()
    module = models.ForeignKey(Module, null=True, blank=True, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"Feedback for {self.module}{self.teacher}"
