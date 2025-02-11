from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from .serializer import SkillSerializer
from .models import Skill as SkillModel


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
