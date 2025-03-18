from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
from django.shortcuts import render
from .models import Video

def index(request):
    videos = Video.objects.all()
    return render(request, 'index.html', {'videos': videos})
