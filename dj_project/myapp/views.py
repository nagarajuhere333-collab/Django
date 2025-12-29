from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Tour

def index(request):
    tours = Tour.objects.all()
    return render(request, 'tours/index.html', {'tours': tours})

# Create your views here.
