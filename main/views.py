from django.shortcuts import redirect
from django.contrib import messages
from .models import About, Services, PortfolioCategory, Photo, Team
from .forms import ContactForm, NewsletterForm
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about = About.objects.all()
        services = Services.objects.filter(is_visible=True)
        categories = PortfolioCategory.objects.all()
        photo = Photo.objects.all()
        team = Team.objects.all()
        form = ContactForm()
        newsletter = NewsletterForm()

        context['about'] = about
        context['services'] = services
        context['title_portfolio'] = 'Portfolio'
        context['p_portfolio'] = 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.'
        context['categories'] = categories
        context['photo'] = photo
        context['title_team'] = 'Team'
        context['p_team'] = 'Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.'
        context['team'] = team
        context['form'] = form
        context['newsletter'] = newsletter

        return context

    def post(self, request, *args, **kwargs):
        if 'submit_form' in request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your message has been sent. Thank you!', extra_tags='contact')
                return redirect('main:index')
            else:
                context = self.get_context_data()
                context['form'] = form
                messages.error(request, 'Please correct the errors.')
                return self.render_to_response(context)

        elif 'submit_newsletter' in request.POST:
            newsletter = NewsletterForm(request.POST)
            if newsletter.is_valid():
                newsletter.save()
                messages.success(request, 'You have signed up for a newsletter!', extra_tags='newsletter')
                return redirect('main:index')
            else:
                context = self.get_context_data()
                context['newsletter'] = newsletter
                return self.render_to_response(context)

        else:
            context = self.get_context_data()
            return self.render_to_response(context)
