from django.shortcuts import redirect
from django.contrib import messages
from .models import About, Services, Counts, PortfolioCategory, Photo, Testimonials, Team
from .forms import ContactForm, NewsletterForm
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    """
        View for return the index page.
        Attributes:
            template_name (str): The name of the template to be used for rendering.
    """
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        """
            Get the context data for return the template.
            Returns:
                 Dict[str, Any]: A dictionary containing the context data.
        """
        context = super().get_context_data(**kwargs)
        about = About.objects.all()
        services = Services.objects.filter(is_visible=True)
        counts = Counts.objects.all()
        categories = PortfolioCategory.objects.all()
        photo = Photo.objects.all()
        testimonials = Testimonials.objects.all()
        team = Team.objects.all()
        form = ContactForm()
        newsletter = NewsletterForm()

        context['title_about'] = 'Voluptatem dignissimos provident quasi'
        context['p_about'] = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                              'incididunt ut labore et dolore magna aliqua. Duis aute irure dolor in reprehenderit')
        context['about'] = about
        context['title_services'] = 'Services'
        context['p_services'] = ('Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum'
                                 ' quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui '
                                 'impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.')
        context['services'] = services
        context['counts'] = counts
        context['title_portfolio'] = 'Portfolio'
        context['p_portfolio'] = ('Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid '
                                  'fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. '
                                  'Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi '
                                  'quidem hic quas.')
        context['categories'] = categories
        context['photo'] = photo
        context['title_testimonials'] = 'Testimonials'
        context['p_testimonials'] = ('Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga'
                                     ' eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et'
                                     ' nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis '
                                     'commodi quidem hic quas.')
        context['testimonials'] = testimonials
        context['title_team'] = 'Team'
        context['p_team'] = ('Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga '
                             'eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui '
                             'impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.')
        context['team'] = team
        context['title_form'] = 'Contact'
        context['p_form'] = ('Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum'
                             ' quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui '
                             'impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.')
        context['form'] = form
        context['newsletter'] = newsletter

        return context

    def post(self, request):
        """
            Handle POST requests.
            Args:
                request: The HTTP request object.
            Returns:
                 Any: The HTTP response.
        """
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you!')
            return redirect('main:index')
        newsletter = NewsletterForm(request.POST)
        if newsletter.is_valid():
            newsletter.save()
            messages.success(request, 'Thank you!')
            return redirect('main:index')
