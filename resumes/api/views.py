from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from resumes.models import Skill, Education, Certificate, Experience, Bio
from resumes.api.serializers import (
    SkillSerializer,
    EducationSerializer,
    CertificateSerializer,
    ExperienceSerializer,
    BioSerializer,
    ResumeSerializer
)

User = get_user_model()


class SkillListCreateAPIView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.objects.select_related('user').filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class SkillRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class EducationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class EducationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class CertificatesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.objects.select_related('user').filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CertificateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class ExperienceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.objects.select_related('user').filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ExperienceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class BioCreateRetrieveUpdateDestroyAPIView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView,
                                            generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return Bio.objects.queryset.objects.select_related('user').filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class ResumeAPIView(generics.RetrieveAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user
