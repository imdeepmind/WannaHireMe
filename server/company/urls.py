from django.urls import path

from .views import ListOrCreateCompany

urlpatterns = [
    path("", ListOrCreateCompany.as_view(), name="Create or List Companies")
]
