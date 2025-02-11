from rest_framework.serializers import ModelSerializer

from .models import (
    EducationalInstitute as EducationalInstituteModel,
    EducationalInstituteLink as EducationalInstituteLinkModel,
)


class EducationalInstituteLinkSerializer(ModelSerializer):
    class Meta:
        model = EducationalInstituteLinkModel
        fields = ["link_type", "url"]


class EducationalInstituteSerializer(ModelSerializer):
    links = EducationalInstituteLinkSerializer(many=True, required=False, source="EducationalInstitute")

    class Meta:
        model = EducationalInstituteModel
        fields = ["name", "description", "logo_uri", "selection_difficulty", "address", "country", "state", "links"]

    def create(self, validated_data):
        links_data = validated_data.pop("EducationalInstitute", [])

        # Create EducationalInstitute
        institute_created_object = EducationalInstituteModel.objects.create(**validated_data)

        # Create EducationalInstituteLink
        link_instances = [
            EducationalInstituteLinkModel(educational_institute=institute_created_object, **link) for link in links_data
        ]
        EducationalInstituteLinkModel.objects.bulk_create(link_instances)

        return institute_created_object
