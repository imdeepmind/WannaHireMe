from django.contrib import admin

from .models import Certification, CertificationLink, CertificationSkill

# Register your models here.
admin.site.register(Certification)
admin.site.register(CertificationLink)
admin.site.register(CertificationSkill)
