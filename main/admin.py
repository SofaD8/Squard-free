from django.contrib import admin
from .models import About, Services, PortfolioCategory, Photo, Team, Contact, Newsletter
from django.utils.safestring import mark_safe


admin.site.register(Contact)
admin.site.register(Newsletter)


# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
        Admin configuration for the 'About' model.
        Attributes:
            list_display (tuple): The fields to display in the list view.
            list_editable (tuple): The fields that can be edited directly in the list view.
            search_fields (tuple): The fields to search by in the admin interface.
    """
    list_display = ('id', 'name', 'description', 'sort')
    list_editable = ('name', 'description', 'sort')
    search_fields = ('name',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    """
        Admin configuration for the 'Services' model.
        Attributes:
            list_display (tuple): The fields to display in the list view.
            list_editable (tuple): The fields that can be edited directly in the list view.
            list_filter (tuple): The fields to filter by in the admin interface.
            search_fields (tuple): The fields to search by in the admin interface.
    """
    list_display = ('id', 'name', 'description', 'is_visible', 'sort')
    list_editable = ('name', 'description', 'is_visible', 'sort')
    list_filter = ('is_visible',)
    search_fields = ('name',)

# ... (similar comments for other registered models)


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'slug')
    list_editable = ('name', 'sort', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'category', 'sort')
    list_editable = ('sort', 'category')
    list_filter = ('category',)
    search_fields = ('sort',)

    def photo_src_tag(self, obj):
        """
            Custom method to display a thumbnail of the photo in the admin list view.
            Args:
                obj: The Team object.
            Returns:
                str: An HTML image tag with the photo.
        """
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

    photo_src_tag.short_description = 'Photo'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'id', 'name', 'description', 'sort')
    list_editable = ('name', 'description', 'sort')
    search_fields = ('name', 'description')

    def photo_src_tag(self, obj):
        """
            Custom method to display a thumbnail of the team photo in the admin list view.
            Args:
                obj: The Team object.
            Returns:
                str: An HTML image tag with the team photo.
        """
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

    photo_src_tag.short_description = 'Team'
