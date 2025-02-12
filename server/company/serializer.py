from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ValidationError

from core.models import LinkType as LinkTypeModel, Country as CountryModel, State as StateModel, Skill as SkillModel
from core.serializer import LinkTypeSerializer, CountrySerializer, StateSerializer, SkillSerializer

from .models import Company as CompanyModel, CompanyLink as CompanyLinkModel, CompanySkill as CompanySkillModel


class CompanyLinkSerializer(ModelSerializer):
    link_type = PrimaryKeyRelatedField(queryset=LinkTypeModel.objects.all(), write_only=True)
    link_type_details = LinkTypeSerializer(source="link_type", read_only=True)

    class Meta:
        model = CompanyLinkModel
        fields = ["link_type", "link_type_details", "url"]


class CompanySkillSerializer(ModelSerializer):
    class Meta:
        model = CompanySkillModel
        fields = ["company", "name"]


class CompanySerializer(ModelSerializer):
    country = PrimaryKeyRelatedField(queryset=CountryModel.objects.all(), write_only=True)
    state = PrimaryKeyRelatedField(queryset=StateModel.objects.all(), write_only=True)

    country_details = CountrySerializer(source="country", read_only=True)
    state_details = StateSerializer(source="state", read_only=True)

    class Meta:
        model = CompanyModel
        fields = [
            "name",
            "description",
            "logo_uri",
            "tier",
            "address",
            "country",
            "country_details",
            "state",
            "state_details",
        ]
