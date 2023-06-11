from rest_framework import serializers

from resumes.models import Skill, Education, Certificate, Experience


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


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'user', 'issuing_authority', 'issue_date']
        read_only_fields = ['user']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'user', 'position', 'start_date', 'end_date', 'description']
        read_only_fields = ['user']
