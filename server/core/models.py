from django.db import models


# Create your models here.
class LinkType(models.Model):
    type = models.CharField(max_length=25)
    logo_uri = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.type}: {self.logo_uri}"


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="Country")

    def __str__(self):
        return self.name
