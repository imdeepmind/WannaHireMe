from django.urls import path

from .views import CreateOrListEducationalInstitutes

urlpatterns = [
    path(
        "",
        CreateOrListEducationalInstitutes.as_view(),
        name="Create or List Educational Institute",
    )
]
