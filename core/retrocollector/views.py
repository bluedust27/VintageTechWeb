from django.shortcuts import render, redirect

from .forms import CollectibleForm
from .models import Collectible


def homepage_view(request):
    return render(request, 'retrocollector/homepage.html')

def collectible_list(request):
    context = {'collectible_list':Collectible.objects.all()}
    return render(request, 'retrocollector/collectible_list.html', context)

def collectible_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = CollectibleForm()
        else:
            collectible = Collectible.objects.get(pk=id)
            form = CollectibleForm(instance=collectible)
        return render(request, 'retrocollector/collectible_form.html', {'form': form})
    else:
        if id == 0:
            form = CollectibleForm(request.POST)
        else:
            collectible = Collectible.objects.get(pk=id)
            form = CollectibleForm(request.POST, instance=collectible)
        if form.is_valid():
            form.save()
        return redirect('/collectibles/list')


def collectible_delete(request, id):
    collectible = Collectible.objects.get(pk=id)
    collectible.delete()
    return redirect('/collectibles/list')
