from django.shortcuts import render

from .models import Mineral

# Create your views here.
def mineral_list(request):
    """Renders list of all the stored minerals."""
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_detail(request):
    """Renders detailed minerals page."""
    return render(request, 'minerals/mineral_detail.html')
