from django.urls import path

from .views import CreateOrListEducationalInstitutes, RetrieveOrUpdateOrDeleteEducationalInstitutes

urlpatterns = [
    path(
        "",
        CreateOrListEducationalInstitutes.as_view(),
        name="Create or List Educational Institute",
    ),
    path(
        "<int:pk>",
        RetrieveOrUpdateOrDeleteEducationalInstitutes.as_view(),
        name="Retrieve or Update or Delete Educational Institute",
    ),
]
