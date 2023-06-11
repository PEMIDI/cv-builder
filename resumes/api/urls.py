from django.urls import path

from .views import (
    SkillListCreateAPIView,
    SkillRetrieveUpdateDestroyAPIView,
    EducationListCreateAPIView,
    EducationRetrieveUpdateDestroyAPIView,
    CertificatesListCreateAPIView,
    CertificateRetrieveUpdateDestroyAPIView,
    ExperienceListCreateAPIView,
    ExperienceRetrieveUpdateDestroyAPIView,
    BioCreateRetrieveUpdateDestroyAPIView,
    ResumeAPIView,
)

urlpatterns = [
    path('', ResumeAPIView.as_view(), name='resume-retrieve')

    path('skills', SkillListCreateAPIView.as_view(), name='skills-list-create'),
    path('skill/<int:pk>', SkillRetrieveUpdateDestroyAPIView.as_view(), name='skill-retrieve-update-destroy'),

    path('educations', EducationListCreateAPIView.as_view(), name='educations-list-create'),
    path('education/<int:pk>', EducationRetrieveUpdateDestroyAPIView.as_view(),
         name='education-retrieve-update-destroy'),

    path('certificates', CertificatesListCreateAPIView.as_view(), name='certificates-list-create'),
    path('certificate/<int:pk>', CertificateRetrieveUpdateDestroyAPIView.as_view(),
         name='certificate-retrieve-update-destroy'),

    path('experiences', ExperienceListCreateAPIView.as_view(), name='experiences-list-create'),
    path('experience/<int:pk>', ExperienceRetrieveUpdateDestroyAPIView.as_view(),
         name='experience-retrieve-update-destroy'),

    path('bio', BioCreateRetrieveUpdateDestroyAPIView.as_view(), name='bio-create-retrieve-update-destroy'),


]
