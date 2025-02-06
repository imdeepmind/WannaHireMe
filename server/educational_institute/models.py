from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import LinkType


class EducationalInstitute(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    logo_uri = models.CharField(max_length=255)
    selection_difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)

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
