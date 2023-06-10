from rest_framework import serializers

from resumes.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'user','title', 'rate', ]
        read_only_fields = ['user']
