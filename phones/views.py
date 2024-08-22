from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_to_query = {
        "name": "name",
        "min_price": "price",
        "max_price": "-price"
    }

    template = 'catalog.html'
    sort = request.GET.get("sort")

    if not sort:
        context = {"phones": map(lambda x: x.__dict__, Phone.objects.all())}
    else:
        context = {"phones": map(lambda x: x.__dict__, Phone.objects.order_by(sort_to_query.get(sort)))}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {"phone": Phone.objects.get(slug=slug).__dict__}
    return render(request, template, context)
