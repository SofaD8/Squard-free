from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Services, PortfolioCategory, Photo, Team, Contact


# Create your views here.
def index(request):
    categories = PortfolioCategory.objects.all()
    for item in categories:
        for photos in item:
            photos.save()

    return HttpResponse('\n'.join(map(str, categories)))