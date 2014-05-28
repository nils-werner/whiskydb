from django.shortcuts import render

from catalog.models import Whisky


def index(request):
    whiskies = Whisky.objects.all()
    context = {'whiskies': whiskies}
    return render(request, 'catalog/index.html', context)


def detail(request, whisky_id):
    whisky = Whisky.objects.get(id=whisky_id)
    context = {'whisky': whisky}
    return render(request, 'catalog/detail.html', context)
