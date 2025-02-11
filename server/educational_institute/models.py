from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import Country, LinkType, Skill, State


class EducationalInstitute(models.Model):
    name = models.CharField(max_length=255, null=False, db_index=True)
    description = models.TextField(blank=True, null=True)
    logo_uri = models.CharField(max_length=255)
    selection_difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)

    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="EducationInstituteCountry")
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="EducationInstituteState")

    def __str__(self):
        return f"Institute {self.name}"


class EducationalInstituteLink(models.Model):
    educational_institute = models.ForeignKey(
        EducationalInstitute, on_delete=models.CASCADE, related_name="EducationalInstitute"
    )
    link_type = models.ForeignKey(LinkType, on_delete=models.CASCADE, related_name="LinkType")
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url


class EducationalInstituteSkill(models.Model):
    educational_institute = models.ForeignKey(
        EducationalInstitute, on_delete=models.CASCADE, related_name="LinkedEducationalInstitute"
    )
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="LinkedSkillEducationalInstitute")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["educational_institute", "skill"], name="unique_education_institute_skills")
        ]

    def __str__(self):
        return f"{self.educational_institute.name} -> {self.skill.name}"
