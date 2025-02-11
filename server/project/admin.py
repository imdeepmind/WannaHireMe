from django.contrib import admin

from .models import Project, ProjectLink, ProjectSkill

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectLink)
admin.site.register(ProjectSkill)
