from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from resumes.api.permissions import IsOwner
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
    """
    💪 API view to list and create skill instances.
    """

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.select_related('user').filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class SkillRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
      💪 API view to retrieve, update, and delete a skill instance.
    """

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class EducationListCreateAPIView(generics.ListCreateAPIView):
    """
    🎓 API view to list and create education instances.
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class EducationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    🎓 API view to retrieve, update, and delete an education instance.
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class CertificatesListCreateAPIView(generics.ListCreateAPIView):
    """
    📜 API view to list and create certificate instances.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return self.queryset.select_related('user').filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CertificateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    📜 API view to retrieve, update, and delete a certificate instance.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class ExperienceListCreateAPIView(generics.ListCreateAPIView):
    """
     🏢 API view to list and create experience instances.
     """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return self.queryset.select_related('user').filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ExperienceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    🏢 API view to retrieve, update, and delete an experience instance.
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class BioCreateRetrieveUpdateDestroyAPIView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView,
                                            generics.UpdateAPIView, generics.DestroyAPIView):
    """
    📝 API view to create, retrieve, update, and delete a bio instance.
    """
    queryset = Bio.objects.all()
    serializer_class = BioSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        return Bio.objects.queryset.select_related('user').filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class ResumeAPIView(generics.RetrieveAPIView):
    """
    📄 API view to retrieve the resume instance of the authenticated user.
    """
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user
