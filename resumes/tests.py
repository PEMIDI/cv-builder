from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from resumes.models import Skill

User = get_user_model()


class SkillsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.skills_url = reverse('resumes:skills-list-create')

    def test_list_skills(self):
        response = self.client.get(self.skills_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_skill(self):
        data = {
            'title': 'Programming',
            'rate': 4
        }
        response = self.client.post(self.skills_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_skill_invalid_rate(self):
        data = {
            'title': 'Programming',
            'rate': 6  # Invalid rate, should fail validation
        }
        response = self.client.post(self.skills_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SkillAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.skill = Skill.objects.create(user=self.user, title='Programming', rate=4)
        self.skill_url = reverse('resumes:skill-retrieve-update-destroy', args=[self.skill.id])

    def test_retrieve_skill(self):
        response = self.client.get(self.skill_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_skill(self):
        data = {
            'title': 'Updated Programming',
            'rate': 5
        }
        response = self.client.put(self.skill_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['rate'], data['rate'])

    def test_delete_skill(self):
        response = self.client.delete(self.skill_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_skill_invalid_rate(self):
        data = {
            'title': 'Updated Programming',
            'rate': 6  # Invalid rate, should fail validation
        }
        response = self.client.put(self.skill_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
