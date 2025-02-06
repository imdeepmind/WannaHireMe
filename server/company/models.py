from django.db import models

from core.models import LinkType


class Company(models.Model):
    TIER_CHOICES = [("tier_1", "Tier 1"), ("tier_2", "Tier 2"), ("tier_3", "Tier 3")]

    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    logo_uri = models.CharField(max_length=255)
    tier = models.CharField(max_length=30, choices=TIER_CHOICES)

    def __str__(self):
        return f"Company {self.name}"


class CompanyLink(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="Company")
    link_type = models.ForeignKey(LinkType, on_delete=models.CASCADE, related_name="LinkTypeCompany")
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url
