from django.shortcuts import render
from django.utils import timezone
from .models import Investigation, BaseForInvestigation


def investigations(request):
    all_inv = Investigation.objects.filter(published_date__lte=timezone.now()).exclude(status='6').order_by(
        '-published_date')
    return render(request, 'investigations/inv_list.html', {'all_inv': all_inv})


def investigations_detail(request, pk):
    basesforinv = BaseForInvestigation.objects.filter(investigation=pk, published_date__lte=timezone.now()).order_by(
        '-published_date')
    return render(request, 'investigations/inv_detail.html', {'basesforinv': basesforinv})
