from django.db import models


# Create your models here.
class Mineral(models.Model):
    """Mineral model table."""
    name = models.CharField(max_length=255, unique=True)
    image_filename = models.CharField(max_length=255)
    image_caption = models.TextField(default='')
    category = models.CharField(max_length=255, default='')
    formula = models.TextField(default='')
    strunz_classification = models.CharField(max_length=255)
    color = models.TextField(default='')
    crystal_system = models.CharField(max_length=255)
    unit_cell = models.CharField(max_length=255)
    crystal_symmetry = models.CharField(max_length=255)
    cleavage = models.CharField(max_length=255)
    mohs_scale_hardness = models.CharField(max_length=255)
    luster = models.CharField(max_length=255)
    streak = models.CharField(max_length=255)
    diaphaneity = models.CharField(max_length=255)
    optical_properties = models.CharField(max_length=255)
    refractive_index = models.CharField(max_length=255)
    crystal_habit = models.TextField(default='')
    specific_gravity = models.CharField(max_length=255)
