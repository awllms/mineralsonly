import random
from django import template

from minerals.models import Mineral

register = template.Library()

@register.simple_tag
def random_mineral():
    """Populates random mineral number."""
    return random.randint(1, Mineral.objects.all().count())
