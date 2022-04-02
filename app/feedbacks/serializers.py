from rest_framework import serializers
from .models import Feedback, Teacher, Module


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'changed_at', 'guid')

    def create(self, validated_data):
        module_id = validated_data.get("module")
        teacher_id = validated_data.get("teacher")
        if module_id:
            module = Module.objects.get(id=module_id)
            feedback = Feedback.objects.create(text=validated_data.get("text"), module=module)

        # if teacher_guid:
        #     teacher = Teacher.objects.get(guid=teacher_guid)
        #     feedback  = Feedback.objects.create(text=validated_data.get("text"), module=teacher)

            return feedback


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
