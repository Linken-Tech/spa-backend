from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from feedback import views

urlpatterns = [
    # get, post feedback list
    path("feedback_details/", views.Feedback.as_view()),
    # get, put, delete feedback details with ID
    path("feedback_details/<pk>/", views.Feedback.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
