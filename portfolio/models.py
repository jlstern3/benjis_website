from django.db import models
import re

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length = 45)
    latin_name = models.CharField(max_length = 45)
    sun = models.CharField(max_length = 45)
    water = models.CharField(max_length = 255)
    spacing = models.IntegerField()
    days_to_harvest = models.IntegerField()
    pH = models.IntegerField()
    planting = models.TextField(null = True)
    soil_reqs = models.TextField(null = True)
    planting = models.TextField(null = True)
    companion_plants = models.TextField(null = True)
    dont_plant_near = models.TextField(null = True)
    pruning = models.TextField(null = True)
    harvesting = models.TextField(null = True)
    common_pests = models.TextField(null = True)
    medicinal_props = models.TextField(null = True)
    edibility = models.TextField(null = True)
    other_uses = models.TextField(null = True)
    specific_notes = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
