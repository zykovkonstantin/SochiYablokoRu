from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Investigation, BaseForInvestigation


def investigations(request):
    all_inv = Investigation.objects.filter(published_date__lte=timezone.now()).exclude(status='6').order_by(
        '-published_date')
    return render(request, 'investigations/inv_list.html', {'all_inv': all_inv})


def investigations_detail(request, pk):
    inv = get_object_or_404(Investigation, pk=pk)
    basesforinv = BaseForInvestigation.objects.filter(investigation=pk, published_date__lte=timezone.now()).order_by(
        '-published_date')
    return render(request, 'investigations/inv_detail.html', {'inv': inv, 'basesforinv': basesforinv})


def base_inv_detail(request, inv_pk, base_pk):
    base = get_object_or_404(BaseForInvestigation, pk=base_pk)
    all_bases = BaseForInvestigation.objects.filter(investigation=inv_pk, published_date__lte=timezone.now()).order_by(
        '-published_date')
    return render(request, 'investigations/base_inv_detail.html', {'base': base, 'all_bases': all_bases})
