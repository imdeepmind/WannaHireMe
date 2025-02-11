from rest_framework.serializers import ModelSerializer

from .models import Skill as SkillModel


class SkillSerializer(ModelSerializer):
    class Meta:
        model = SkillModel
        fields = "__all__"
