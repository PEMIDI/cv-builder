from rest_framework import serializers

from resumes.models import Skill, Education


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'user', 'title', 'rate', ]
        read_only_fields = ['user']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'user', 'institution', 'degree', 'start_date', 'end_date', ]
        read_only_fields = ['user']
