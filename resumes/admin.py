from django.contrib import admin
from .models import Skill, Education, Certificate, Experience, Bio

admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(Experience)
admin.site.register(Bio)
