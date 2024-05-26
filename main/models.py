from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        ordering = ['sort']


class Services(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['sort']


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __iter__(self):
        for photo in self.photo.all():
            yield photo

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Portfolio Category'
        verbose_name_plural = 'Portfolio Categories'
        ordering = ['sort']


class Photo(models.Model):
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='photo',
                                 null=True, blank=True)
    sort = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)

    def __int__(self):
        return self.sort

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
        ordering = ['sort']


class Team(models.Model):
    name = models.CharField(max_length=300, unique=True)
    description = RichTextField(blank=True, null=True)
    sort = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'
        ordering = ['sort']


class Contact(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
        ordering = ['-date_created']
