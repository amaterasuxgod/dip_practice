from django.shortcuts import render
from .models import Pc

# Create your views here.


def indexView(request):
    pcs = Pc.objects.all()
    context = {
        'items': pcs
    }
    return render(request, 'products.html', context)
