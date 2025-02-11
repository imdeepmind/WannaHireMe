from django.urls import path

from .views import RetrieveOrEditOrDeleteSkill, CreateOrListSkill

urlpatterns = [
    path("", CreateOrListSkill.as_view(), name="Create or List Skills"),
    path("<int:pk>", RetrieveOrEditOrDeleteSkill.as_view(), name="Retrieve or Edit or Delete Skill"),
]
