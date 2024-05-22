from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Services, PortfolioCategory, Photo, Team, Contact


# Create your views here.
def index(request):
    categories = PortfolioCategory.objects.all()
    photo = Photo.objects.all()

    context = {
        'title_portfolio': 'Portfolio',
        'p_portfolio': 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'categories': categories,
        'photos': photo,
        'title_team': 'Team',
        'p_team': 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.',
        'team': Team.objects.all(),

    }

    return render(request, 'main.html', context=context)