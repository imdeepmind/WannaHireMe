from django.db.models import Q

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Company as CompanyModel
from .serializer import CompanySerializer


class ListOrCreateCompany(ListCreateAPIView):
    queryset = CompanyModel.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = CompanySerializer


class RetrieveOrUpdateOrDeleteCompany(RetrieveUpdateDestroyAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer


class SearchCompany(ReadOnlyModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        queryset = CompanyModel.objects.all()
        request = self.request
        params = request.GET

        query = params.get("query")
        sortField = params.get('sort')
        sortOrder = params.get('order')

        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

        if sortField:
            if sortOrder == "desc":
                queryset = queryset.order_by(f"-{sortField}")
            else:
                queryset = queryset.order_by(f"{sortField}")

        return queryset
