from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Skill as SkillModel, LinkType as LinkTypeModel, Country as CountryModel, State as StateModel


class SkillSerializer(ModelSerializer):
    class Meta:
        model = SkillModel
        fields = "__all__"


class LinkTypeSerializer(ModelSerializer):
    class Meta:
        model = LinkTypeModel
        fields = "__all__"


class CountrySerializer(ModelSerializer):
    class Meta:
        model = CountryModel
        fields = "__all__"


class StateSerializer(ModelSerializer):
    country_name = SerializerMethodField(read_only=True)
    country_id = SerializerMethodField(read_only=True)

    class Meta:
        model = StateModel
        fields = ["id", "name", "country_name", "country_id"]

    def get_country_name(self, obj):
        return obj.country.name

    def get_country_id(self, obj):
        return obj.country.id
