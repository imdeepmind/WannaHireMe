from django.urls import path

from .views import ListOrCreateCompany, RetrieveOrUpdateOrDeleteCompany

urlpatterns = [
    path("", ListOrCreateCompany.as_view(), name="Create or List Companies"),
    path("<int:pk>", RetrieveOrUpdateOrDeleteCompany.as_view(), name="Retrieve or Update or Delete Company")
]
