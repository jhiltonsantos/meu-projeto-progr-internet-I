from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bemvindo(request):
    return render(request, 'bemvindo.html')
