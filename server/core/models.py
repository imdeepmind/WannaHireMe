from django.db import models


# Create your models here.
class LinkType(models.Model):
    type = models.CharField(max_length=25)
    logo_uri = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.type}: {self.logo_uri}"
