from django.db import models
from django.db import IntegrityError


# Create your models here.
class Mineral(models.Model):
    """Mineral model table."""
    name = models.CharField(max_length=255, unique=True)
    image_filename = models.CharField(max_length=255)
    image_caption = models.TextField(blank=True, default='')
    category = models.CharField(max_length=255, blank=True, default='')
    formula = models.TextField(blank=True, default='')
    strunz_classification = models.CharField(max_length=255, blank=True, default='')
    color = models.TextField(blank=True, default='')
    crystal_system = models.CharField(max_length=255, blank=True, default='')
    unit_cell = models.CharField(max_length=255, blank=True, default='')
    crystal_symmetry = models.CharField(max_length=255, blank=True, default='')
    cleavage = models.CharField(max_length=255, blank=True, default='')
    mohs_scale_hardness = models.CharField(max_length=255, blank=True, default='')
    luster = models.CharField(max_length=255, blank=True, default='')
    streak = models.CharField(max_length=255, blank=True, default='')
    diaphaneity = models.CharField(max_length=255, blank=True, default='')
    optical_properties = models.CharField(max_length=255, blank=True, default='')
    refractive_index = models.CharField(max_length=255, blank=True, default='')
    crystal_habit = models.TextField(blank=True, default='')
    specific_gravity = models.CharField(max_length=255, blank=True, default='')
    group = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.name


def load_json_data():
    """Reads the json file in the assets folder.
    Then loads data into database.
    """
    import json
    with open('assets/minerals.json') as mineralfile:
        mineral_list_data = json.load(mineralfile)
    for mineral in mineral_list_data:
        try:
            Mineral.objects.create(**mineral)
        except IntegrityError:
            pass
