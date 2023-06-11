from django.urls import path

from .views import SkillListCreateAPIView, SkillRetrieveUpdateDestroyAPIView, EducationListCreateAPIView

urlpatterns = [
    path('skills', SkillListCreateAPIView.as_view(), name='skills-list-create'),
    path('skills/<int:pk>', SkillRetrieveUpdateDestroyAPIView.as_view(), name='skill-retrieve-update-destroy'),

    path('educations', EducationListCreateAPIView.as_view(), name='educations-list-create')
]
