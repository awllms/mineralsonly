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


@register.inclusion_tag('minerals/group_nav.html', takes_context=True)
def group_nav_list(context):
    """Returns dictionary of minerals to display as group nav pane."""
    minerals = Mineral.objects.values_list('group', flat=True).distinct()
    return {'minerals': minerals, 'request': context['request']}


@register.filter('strip_white_space')
def strip_white_space(mineral_name):
    """Strips whitespace on words."""
    mineral = mineral_name.replace(" ", "-")
    return mineral
