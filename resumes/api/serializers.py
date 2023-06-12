from django.contrib.auth import get_user_model
from rest_framework import serializers

from resumes.models import Skill, Education, Certificate, Experience, Bio

User = get_user_model()


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
        fields = ['id', 'user', 'company', 'position', 'start_date', 'end_date', 'description']
        read_only_fields = ['user']


class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = ['id', 'user', 'content']
        read_only_fields = ['user', ]


class ResumeSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    educations = EducationSerializer(many=True)
    certificates = CertificateSerializer(many=True)
    experiences = ExperienceSerializer(many=True)
    bio = BioSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'skills', 'educations', 'certificates',
                  'experiences', 'bio']
