from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from resumes.api.serializers import SkillSerializer
from resumes.models import Skill


class SkillListCreateAPIView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated, ]
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


