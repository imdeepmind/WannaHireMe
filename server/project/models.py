from django.db import models

from core.models import LinkType, Skill


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class ProjectLink(models.Model):
    company = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="Project")
    link_type = models.ForeignKey(LinkType, on_delete=models.CASCADE, related_name="ProjectLinkType")
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url


class ProjectSkill(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="LinkedProject")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="LinkedSkill")

    class Meta:
        constraints = [models.UniqueConstraint(fields=["project", "skill"], name="unique_project_skill")]

    def __str__(self):
        return f"{self.project.name} -> {self.skill.name}"
