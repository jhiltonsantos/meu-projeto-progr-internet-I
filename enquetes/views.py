from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from enquetes.models import Enquete


def bemvindo(request):
    return render(request, 'bemvindo.html')


def enquete(request, enquete_id):
    enquete = {'enquete': get_object_or_404(Enquete, id=enquete_id)}

    return render(request, 'enquete.html', enquete)
