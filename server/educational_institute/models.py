from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import Country, LinkType, State


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
        EducationalInstitute, on_delete=models.CASCADE, related_name="educational_institute_links"
    )
    link_type = models.ForeignKey(LinkType, on_delete=models.CASCADE, related_name="educational_institute_link_type")
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url
