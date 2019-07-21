import random
from django import template

from minerals.models import Mineral

from minerals.alphabet_list import ALPHABET_LIST as letters_list

register = template.Library()


@register.simple_tag
def random_mineral():
    """Populates random mineral number."""
    return random.randint(1, Mineral.objects.all().count())


@register.simple_tag
def show_letters():
    """A template tag that returns a list a letters."""
    letters = letters_list
    return letters
