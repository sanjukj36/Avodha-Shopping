from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import product,categ
from django.core.paginator import Paginator


def home(request,c_slug=None):
    c_page = None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prodt = product.objects.filter(category=c_page, avilable=True)
    else:
        prodt = product.objects.all().filter(avilable=True)
    cat=categ.objects.all()

    paginator = Paginator(prodt, 3)  # Show 2 contacts per page.
    page_number = int(request.GET.get('page', '1'))
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {"pr": prodt,'ct':cat,'page_obj':page_obj})



def prodDetails(request, c_slug, product_slug):
    try:
        prod = product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'items.html', {"pr": prod})



def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = product.objects.all().filter(Q(name__contains=query) | Q(dec__contains=query))
    return render(request, 'search.html', {'pr': prod, 'qr': query})
