from django.shortcuts import render

from .models import Mineral

# Create your views here.
def mineral_list(request):
    """Renders list of all the stored minerals."""
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    """Renders detailed minerals page."""
    mineral = Mineral.objects.filter(pk=pk)
    return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})
