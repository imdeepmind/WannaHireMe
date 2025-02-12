from django.db import models

from core.models import LinkType, Country, Skill, State


class Company(models.Model):
    TIER_CHOICES = [("tier_1", "Tier 1"), ("tier_2", "Tier 2"), ("tier_3", "Tier 3")]

    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    logo_uri = models.CharField(max_length=255)
    tier = models.CharField(max_length=30, choices=TIER_CHOICES)

    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="CompanyCountry")
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="CompanyState")

    def __str__(self):
        return f"Company {self.name}"


class CompanyLink(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_links_for_link")
    link_type = models.ForeignKey(LinkType, on_delete=models.CASCADE, related_name="company_link_type")
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url


class CompanySkill(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_skill_company")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="company_skill_skill")

    class Meta:
        constraints = [models.UniqueConstraint(fields=["company", "skill"], name="unique_company_skill")]

    def __str__(self):
        return f"{self.company.name} -> {self.skill.name}"
