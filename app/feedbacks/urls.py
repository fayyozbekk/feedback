from django.urls import path

from .views import FeedbackList, TeacherList, TeacherDetail, FeedbackForTeacherList, ModuleDetail, FeedbackForModuleList, ModuleList

urlpatterns = [
    path("api/feedbacks/", FeedbackList.as_view()),
    path("api/teachers/", TeacherList.as_view()),
    path("api/teachers/<uuid:guid>/", TeacherDetail.as_view()),
    path("api/teachers/<uuid:guid>/feedbacks/", FeedbackForTeacherList.as_view()),
    path("api/modules/", ModuleList.as_view()),
    path("api/modules/<uuid:guid>/", ModuleDetail.as_view()),
    path("api/modules/<uuid:guid>/feedbacks/", FeedbackForModuleList.as_view()),
]
