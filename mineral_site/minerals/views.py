from django.shortcuts import render, get_object_or_404

from .models import Mineral

# Create your views here.
def mineral_list(request):
    """Renders list of all the stored minerals starting
    with the letter 'a'."""
    minerals = Mineral.objects.filter(name__istartswith='a')
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    """Renders detailed minerals page."""
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})


def letter_search(request, letter):
    """Display minerals by letter."""
    minerals = Mineral.objects.filter(name__istartswith=letter)
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})
