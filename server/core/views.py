from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Skill as SkillModel, LinkType as LinkTypeModel, Country as CountryModel, State as StateModel
from .serializer import SkillSerializer, CountrySerializer, StateSerializer, LinkTypeSerializer


# Create your views here.
class CreateOrListSkill(ListCreateAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializer
    pagination_class = PageNumberPagination
    # TODO: Add permission


class RetrieveOrEditOrDeleteSkill(RetrieveUpdateDestroyAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializer
    # TODO: Add permission


class CreateOrListLinkType(ListCreateAPIView):
    queryset = LinkTypeModel.objects.all()
    serializer_class = LinkTypeSerializer
    pagination_class = PageNumberPagination
    # TODO: Add permission


class RetrieveOrEditOrDeleteLinkType(RetrieveUpdateDestroyAPIView):
    queryset = LinkTypeModel.objects.all()
    serializer_class = LinkTypeSerializer
    # TODO: Add permission


class CreateOrListCountry(ListCreateAPIView):
    queryset = CountryModel.objects.all()
    serializer_class = CountrySerializer
    pagination_class = PageNumberPagination
    # TODO: Add permission


class RetrieveOrEditOrDeleteCountry(RetrieveUpdateDestroyAPIView):
    queryset = CountryModel.objects.all()
    serializer_class = CountrySerializer
    # TODO: Add permission


class CreateOrListState(ListCreateAPIView):
    queryset = StateModel.objects.all()
    serializer_class = StateSerializer
    pagination_class = PageNumberPagination
    # TODO: Add permission


class RetrieveOrEditOrDeleteState(RetrieveUpdateDestroyAPIView):
    queryset = StateModel.objects.all()
    serializer_class = StateSerializer
    # TODO: Add permission
