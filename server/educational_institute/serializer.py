from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ValidationError

from core.serializer import CountrySerializer, StateSerializer, LinkTypeSerializer
from core.models import Country as CountryModel, State as StateModel, LinkType as LinkTypeModel

from .models import (
    EducationalInstitute as EducationalInstituteModel,
    EducationalInstituteLink as EducationalInstituteLinkModel,
)


class EducationalInstituteLinkSerializer(ModelSerializer):
    link_type = PrimaryKeyRelatedField(queryset=LinkTypeModel.objects.all(), write_only=True)

    link_type_details = LinkTypeSerializer(source="link_type", read_only=True)

    class Meta:
        model = EducationalInstituteLinkModel
        fields = ["link_type", "link_type_details", "url"]


class EducationalInstituteSerializer(ModelSerializer):
    country = PrimaryKeyRelatedField(queryset=CountryModel.objects.all(), write_only=True)
    state = PrimaryKeyRelatedField(queryset=StateModel.objects.all(), write_only=True)

    country_details = CountrySerializer(source="country", read_only=True)
    state_details = StateSerializer(source="state", read_only=True)

    links = EducationalInstituteLinkSerializer(many=True, required=False, source="educational_institute_links")

    class Meta:
        model = EducationalInstituteModel
        fields = [
            "name",
            "description",
            "logo_uri",
            "selection_difficulty",
            "address",
            "country",
            "state",
            "country_details",
            "state_details",
            "links",
        ]

    def validate_links(self, links):
        if len(links) > 5:
            raise ValidationError("Only 5 links can be added")

        return links

    def create(self, validated_data):
        links_data = validated_data.pop("educational_institute_links", [])

        if len(links_data) > 5:
            raise ValidationError("Only 5 links can be added")

        country = validated_data.pop("country")
        state = validated_data.pop("state")

        # Create the EducationalInstituteModel instance
        instance = EducationalInstituteModel.objects.create(
            country=country, state=state, **validated_data  # Pass remaining fields dynamically
        )

        link_instances = [EducationalInstituteLinkModel(educational_institute=instance, **link) for link in links_data]
        EducationalInstituteLinkModel.objects.bulk_create(link_instances)

        return instance

    def update(self, instance, validated_data):
        links_data = validated_data.pop("educational_institute_links", [])

        if len(links_data) > 5:
            raise ValidationError("Only 5 links can be added")

        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.logo_uri = validated_data.get("logo_uri", instance.logo_uri)
        instance.selection_difficulty = validated_data.get("selection_difficulty", instance.selection_difficulty)
        instance.address = validated_data.get("address", instance.address)

        instance.country = validated_data.get("country", instance.country)
        instance.state = validated_data.get("state", instance.state)

        instance.save()

        if links_data:
            existing_link_ids = [link.id for link in instance.educational_institute_links.all()]

            EducationalInstituteLinkModel.objects.filter(id__in=existing_link_ids).delete()
            EducationalInstituteLinkModel.objects.bulk_create(
                [EducationalInstituteLinkModel(educational_institute=instance, **link) for link in links_data]
            )

        return instance
