from django.shortcuts import render

# Create your views here.
def mineral_list(request):
    """Renders list of all the stored minerals."""
    return render(request, 'minerals/mineral_list.html')


def mineral_detail(request):
    """Renders detailed minerals page."""
    return render(request, 'minerals/mineral_detail.html')
