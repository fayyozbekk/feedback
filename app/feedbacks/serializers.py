from rest_framework import serializers
from .models import Feedback, Teacher, Module


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'changed_at', 'guid')


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"
        read_only_fields = ('id', 'created_at', 'changed_at', 'guid')


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = "__all__"
        read_only_fields = ('id', 'created_at', 'changed_at', 'guid')
