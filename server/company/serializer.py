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
    skill = PrimaryKeyRelatedField(queryset=SkillModel.objects.all(), write_only=True)
    skill_details = SkillSerializer(source="skill", read_only=True)

    class Meta:
        model = CompanySkillModel
        fields = ["skill", "skill_details"]


class CompanySerializer(ModelSerializer):
    country = PrimaryKeyRelatedField(queryset=CountryModel.objects.all(), write_only=True)
    state = PrimaryKeyRelatedField(queryset=StateModel.objects.all(), write_only=True)

    country_details = CountrySerializer(source="country", read_only=True)
    state_details = StateSerializer(source="state", read_only=True)

    links = CompanyLinkSerializer(many=True, required=False, source="company_links_for_link")
    skills = CompanySkillSerializer(many=True, required=False, source="company_skill_company")

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
            "links",
            "skills",
        ]

    def validate_links(self, links):
        if len(links) > 5:
            raise ValidationError("Only 5 links can be added")

        return links

    def validate_skills(self, skills):
        if len(skills) > 10:
            raise ValidationError("Only 10 skills can be added")

        return skills

    def create(self, validated_data):
        links_data = validated_data.pop("company_links_for_link", [])
        skills_data = validated_data.pop("company_skill_company", [])

        if len(links_data) > 5:
            raise ValidationError("Only 5 links can be added")

        if len(skills_data) > 10:
            raise ValidationError("Only 10 skills can be added")

        country = validated_data.pop("country")
        state = validated_data.pop("state")

        instance = CompanyModel.objects.create(country=country, state=state, **validated_data)

        CompanyLinkModel.objects.bulk_create(
            [
                CompanyLinkModel(
                    company=instance,
                    **link,
                )
                for link in links_data
            ]
        )

        CompanySkillModel.objects.bulk_create([CompanySkillModel(company=instance, **skill) for skill in skills_data])

        return instance

    def update(self, instance, validated_data):
        links_data = validated_data.pop("company_links_for_link", [])
        skills_data = validated_data.pop("company_skill_company", [])

        if len(links_data) > 5:
            raise ValidationError("Only 5 links can be added")

        if len(skills_data) > 10:
            raise ValidationError("Only 10 skills can be added")

        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.logo_uri = validated_data.get("logo_uri", instance.logo_uri)
        instance.tier = validated_data.get("tier", instance.tier)

        instance.address = validated_data.get("address", instance.address)
        instance.country = validated_data.get("country", instance.country)
        instance.state = validated_data.get("state", instance.state)

        instance.save()

        if links_data:
            existing_link_ids = [link.id for link in instance.company_links_for_link.all()]

            CompanyLinkModel.objects.filter(id__in=existing_link_ids).delete()
            CompanyLinkModel.objects.bulk_create([CompanyLinkModel(company=instance, **link) for link in links_data])

        if skills_data:
            existing_skill_ids = [skill.id for skill in instance.company_skill_company.all()]

            CompanySkillModel.objects.filter(id__in=existing_skill_ids).delete()
            CompanySkillModel.objects.bulk_create(
                [CompanySkillModel(company=instance, **skill) for skill in skills_data]
            )

        return instance
