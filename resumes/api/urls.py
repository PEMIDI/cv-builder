from django.urls import path

from .views import SkillListCreateAPIView, SkillRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('skills', SkillListCreateAPIView.as_view(), name='skills-list-create'),
    path('skill/<int:pk>', SkillRetrieveUpdateDestroyAPIView.as_view(), name='skill-retrieve-update-destroy')
]