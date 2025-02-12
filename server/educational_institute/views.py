from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from .models import (
    EducationalInstitute as EducationalInstituteModel,
)
from .serializer import EducationalInstituteSerializer


# Create your views here.
class CreateOrListEducationalInstitutes(ListCreateAPIView):
    queryset = EducationalInstituteModel.objects.all()
    serializer_class = EducationalInstituteSerializer
    pagination_class = PageNumberPagination

class RetrieveOrUpdateOrDeleteEducationalInstitutes(RetrieveUpdateDestroyAPIView):
    queryset = EducationalInstituteModel.objects.all()
    serializer_class = EducationalInstituteSerializer
