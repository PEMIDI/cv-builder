from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from resumes.models import Skill, Education, Certificate, Experience, Bio

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


class EducationsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.education = Education.objects.create(
            user=self.user,
            institution='University',
            degree='Bachelor',
            start_date='2020-01-01',
            end_date='2023-01-01'
        )
        self.education_url = reverse('resumes:educations-list-create')

    def test_list_educations(self):
        response = self.client.get(self.education_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_education(self):
        data = {
            'institution': 'College',
            'degree': 'Associate',
            'start_date': '2018-01-01',
            'end_date': '2020-01-01'
        }
        response = self.client.post(self.education_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['institution'], data['institution'])
        self.assertEqual(response.data['degree'], data['degree'])
        self.assertEqual(response.data['start_date'], data['start_date'])
        self.assertEqual(response.data['end_date'], data['end_date'])


class EducationAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.education = Education.objects.create(
            user=self.user,
            institution='University',
            degree='Bachelor',
            start_date='2020-01-01',
            end_date='2023-01-01'
        )
        self.education_detail_url = reverse('resumes:education-retrieve-update-destroy', args=[self.education.pk])

    def test_retrieve_education(self):
        response = self.client.get(self.education_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['institution'], self.education.institution)
        self.assertEqual(response.data['degree'], self.education.degree)
        self.assertEqual(response.data['start_date'], str(self.education.start_date))
        self.assertEqual(response.data['end_date'], str(self.education.end_date))

    def test_update_education(self):
        data = {
            'institution': 'College',
            'degree': 'Associate',
            'start_date': '2018-01-01',
            'end_date': '2020-01-01'
        }
        response = self.client.put(self.education_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['institution'], data['institution'])
        self.assertEqual(response.data['degree'], data['degree'])
        self.assertEqual(response.data['start_date'], data['start_date'])
        self.assertEqual(response.data['end_date'], data['end_date'])

    def test_delete_education(self):
        response = self.client.delete(self.education_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Education.objects.filter(pk=self.education.pk).exists())


class CertificateAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.certificate = Certificate.objects.create(
            user=self.user,
            issuing_authority='Authority',
            issue_date='2022-01-01'
        )
        self.certificate_detail_url = reverse('resumes:certificate-retrieve-update-destroy', args=[self.certificate.pk])

    def test_list_certificates(self):
        response = self.client.get(reverse('resumes:certificates-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['issuing_authority'], self.certificate.issuing_authority)
        self.assertEqual(response.data[0]['issue_date'], str(self.certificate.issue_date))

    def test_create_certificate(self):
        data = {
            'issuing_authority': 'New Authority',
            'issue_date': '2023-01-01'
        }
        response = self.client.post(reverse('resumes:certificates-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['issuing_authority'], data['issuing_authority'])
        self.assertEqual(response.data['issue_date'], data['issue_date'])

    def test_retrieve_certificate(self):
        response = self.client.get(self.certificate_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['issuing_authority'], self.certificate.issuing_authority)
        self.assertEqual(response.data['issue_date'], str(self.certificate.issue_date))

    def test_update_certificate(self):
        data = {
            'issuing_authority': 'Updated Authority',
            'issue_date': '2024-01-01'
        }
        response = self.client.put(self.certificate_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['issuing_authority'], data['issuing_authority'])
        self.assertEqual(response.data['issue_date'], data['issue_date'])

    def test_delete_certificate(self):
        response = self.client.delete(self.certificate_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Certificate.objects.filter(pk=self.certificate.pk).exists())


class ExperienceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.experience = Experience.objects.create(
            user=self.user,
            company='Company',
            position='Position',
            start_date='2022-01-01',
            end_date='2022-12-31',
            description='Experience description'
        )
        self.experience_detail_url = reverse('resumes:experience-retrieve-update-destroy', args=[self.experience.pk])

    def test_list_experiences(self):
        response = self.client.get(reverse('resumes:experiences-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['company'], self.experience.company)
        self.assertEqual(response.data[0]['position'], self.experience.position)
        self.assertEqual(response.data[0]['start_date'], str(self.experience.start_date))
        self.assertEqual(response.data[0]['end_date'], str(self.experience.end_date))
        self.assertEqual(response.data[0]['description'], self.experience.description)

    def test_create_experience(self):
        data = {
            'company': 'New Company',
            'position': 'New Position',
            'start_date': '2023-01-01',
            'end_date': '2023-12-31',
            'description': 'New experience description'
        }
        response = self.client.post(reverse('resumes:experiences-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['company'], data['company'])
        self.assertEqual(response.data['position'], data['position'])
        self.assertEqual(response.data['start_date'], data['start_date'])
        self.assertEqual(response.data['end_date'], data['end_date'])
        self.assertEqual(response.data['description'], data['description'])

    def test_retrieve_experience(self):
        response = self.client.get(self.experience_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['company'], self.experience.company)
        self.assertEqual(response.data['position'], self.experience.position)
        self.assertEqual(response.data['start_date'], str(self.experience.start_date))
        self.assertEqual(response.data['end_date'], str(self.experience.end_date))
        self.assertEqual(response.data['description'], self.experience.description)

    def test_update_experience(self):
        data = {
            'company': 'Updated Company',
            'position': 'Updated Position',
            'start_date': '2024-01-01',
            'end_date': '2024-12-31',
            'description': 'Updated experience description'
        }
        response = self.client.put(self.experience_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['company'], data['company'])
        self.assertEqual(response.data['position'], data['position'])
        self.assertEqual(response.data['start_date'], data['start_date'])
        self.assertEqual(response.data['end_date'], data['end_date'])
        self.assertEqual(response.data['description'], data['description'])

    def test_delete_experience(self):
        response = self.client.delete(self.experience_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Experience.objects.filter(pk=self.experience.pk).exists())


class ResumeAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.resume_url = reverse('resumes:resume-retrieve')
        self.skills_url = reverse('resumes:skills-list-create')
        self.educations_url = reverse('resumes:educations-list-create')
        self.certificates_url = reverse('resumes:certificates-list-create')
        self.experiences_url = reverse('resumes:experiences-list-create')

        # Create a bio object and associate it with the user
        self.bio = Bio.objects.create(user=self.user, content='Bio content')
        self.bio_url = reverse('resumes:bio-create-retrieve-update-destroy')

    def test_retrieve_resume(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.resume_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert response data
        self.assertEqual(response.data['first_name'], self.user.first_name)
        self.assertEqual(response.data['last_name'], self.user.last_name)
        self.assertEqual(response.data['email'], self.user.email)
        self.assertEqual(response.data['phone_number'], self.user.phone_number)
        self.assertEqual(len(response.data['skills']), self.user.skills.count())
        self.assertEqual(len(response.data['educations']), self.user.educations.count())
        self.assertEqual(len(response.data['certificates']), self.user.certificates.count())
        self.assertEqual(len(response.data['experiences']), self.user.experiences.count())
        self.assertEqual(response.data['bio']['content'], self.bio.content)