from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Feedback, Teacher, Module
from .serializers import FeedbackSerializer, TeacherSerializer, ModuleSerializer, FSerializer


class FeedbackList(APIView):
    def post(self, request, format=None):
        serializer = FSerializer(data=request.data)
        if serializer.is_valid():
            module = Module.objects.get(guid=serializer.validated_data["module"])
            Feedback.objects.create(text=serializer.validated_data["text"], module=module)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherList(APIView):
    def get(self, request, format=None):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeacherDetail(APIView):
    def get_object(self, guid):
        try:
            return Teacher.objects.get(guid=guid)
        except Teacher.DoesNotExist:
            raise Http404

    def get(self, request, guid, format=None):
        teacher = self.get_object(guid=guid)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)


class FeedbackForTeacherList(APIView):
    def get(self, reqeust, guid, format=None):
        feedbacks = self.get_queryset(guid=guid)
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self, guid):
        try:
            teacher = Teacher.objects.get(guid=guid)
            return Feedback.objects.filter(teacher=teacher)
        except Teacher.DoesNotExist:
            raise Http404


class ModuleList(APIView):
    def get(self, request, format=None):
        modules = Module.objects.all()
        serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ModuleDetail(APIView):
    def get_object(self, guid):
        try:
            return Module.objects.get(guid=guid)
        except Module.DoesNotExist:
            raise Http404

    def get(self, request, guid, format=None):
        module = self.get_object(guid=guid)
        serializer = ModuleSerializer(module)
        return Response(serializer.data)


class FeedbackForModuleList(APIView):
    def get(self, reqeust, guid, format=None):
        feedbacks = self.get_queryset(guid=guid)
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self, guid):
        try:
            module = Module.objects.get(guid=guid)
            return Feedback.objects.filter(module=module)
        except Module.DoesNotExist:
            raise Http404
