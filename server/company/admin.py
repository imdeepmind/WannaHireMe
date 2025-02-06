from django.contrib import admin

from .models import Company, CompanyLink

# Register your models here.
admin.site.register(Company)
admin.site.register(CompanyLink)
