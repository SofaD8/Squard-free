from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class About(models.Model):
    """
        Model representing information about the company or organization.
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        ordering = ['sort']


class Services(models.Model):
    """
        Model representing services offered by the company.
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['sort']


class Counts(models.Model):
    """
        Model representing count of services offered by the company.
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.CharField(max_length=100, null=True, blank=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Count'
        verbose_name_plural = 'Counts'
        ordering = ['sort']


class PortfolioCategory(models.Model):
    """
       Model representing categories for the portfolio.
    """
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
    """
        Model representing photos in the portfolio.
    """
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


class Testimonials(models.Model):
    """
        Model representing test imonials.
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    review = RichTextField(null=True, blank=True)
    sort = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='testimonials/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['sort']


class Team(models.Model):
    """
        Model representing team members.
    """
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
    """
        Model representing contact form submissions.
    """
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


class Newsletter(models.Model):
    """
        Model representing newsletter subscribers.
    """
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
        ordering = ['email']
