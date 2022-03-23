from django.contrib import admin
from .models import Teacher, Student, Module, Feedback


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "module", "is_leader", "created_at", "changed_at"]
    list_display = ["guid", "module", "is_leader", "created_at", "changed_at"]
    readonly_fields = ["created_at", "changed_at"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "guid", "is_scholarship", "level", "created_at", "changed_at"]
    list_display = ["guid", "is_scholarship", "level", "created_at", "changed_at"]
    readonly_fields = ["created_at", "changed_at"]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    fields = ["guid", "name", "description", "created_at", "changed_at"]
    list_display = ["guid", "name", "description", "created_at", "changed_at"]
    readonly_fields = ["created_at", "changed_at"]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    fields = ["module", "text", "teacher", "created_at", "changed_at"]
    list_display = ["guid", "module", "text", "teacher", "created_at", "changed_at"]
    readonly_fields = ["created_at", "changed_at"]
