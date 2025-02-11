from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import LinkType, Skill


# Create your models here.
class Certification(models.Model):
    name = models.CharField(max_length=255, null=False, db_index=True)
    description = models.TextField(blank=True, null=True)
    logo_uri = models.CharField(max_length=255)
    completion_difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)

    certification_id = models.CharField(max_length=255, null=True)
    certification_url = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class CertificationLink(models.Model):
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE, related_name="Certification")
    link_type = models.ForeignKey(LinkType, on_delete=models.CASCADE, related_name="CertificationLinkType")
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url


class CertificationSkill(models.Model):
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE, related_name="LinkedCertification")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="LinkedSkillCertification")

    class Meta:
        constraints = [models.UniqueConstraint(fields=["certification", "skill"], name="unique_certification_skill")]

    def __str__(self):
        return f"{self.certification.name} -> {self.skill.name}"
