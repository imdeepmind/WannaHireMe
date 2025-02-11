from django.contrib import admin

from .models import EducationalInstitute, EducationalInstituteLink, EducationalInstituteSkill

# Register your models here.
admin.site.register(EducationalInstitute)
admin.site.register(EducationalInstituteLink)
admin.site.register(EducationalInstituteSkill)
