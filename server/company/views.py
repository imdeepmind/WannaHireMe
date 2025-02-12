from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Company as CompanyModel
from .serializer import CompanySerializer


class ListOrCreateCompany(ListCreateAPIView):
    queryset = CompanyModel.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = CompanySerializer
