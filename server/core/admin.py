from django.contrib import admin

from .models import LinkType, Country, Skill, State

# Register your models here.
admin.site.register(LinkType)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Skill)
