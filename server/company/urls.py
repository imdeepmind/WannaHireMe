from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ListOrCreateCompany, RetrieveOrUpdateOrDeleteCompany, SearchCompany

router = DefaultRouter()
router.register(r'companies', SearchCompany, basename='company')

urlpatterns = [
    path("", ListOrCreateCompany.as_view(), name="Create or List Companies"),
    path("<int:pk>", RetrieveOrUpdateOrDeleteCompany.as_view(), name="Retrieve or Update or Delete Company"),
    path("search/", include(router.urls))
]
