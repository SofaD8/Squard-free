from django.contrib import admin
from .models import About, Services, PortfolioCategory, Photo, Team, Contact


# Register your models here.
admin.site.register(About)
admin.site.register(Services)
admin.site.register(PortfolioCategory)
admin.site.register(Photo)
admin.site.register(Team)
admin.site.register(Contact)