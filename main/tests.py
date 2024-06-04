from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import About, Services, PortfolioCategory, Photo, Team, Contact, Newsletter
from .views import IndexView
from .forms import ContactForm, NewsletterForm


# models tests
class ModelsTestCase(TestCase):
    def setUp(self):
        self.about = About.objects.create(name='Test about', description='This is a test description', sort=1)
        self.services = Services.objects.create(name='Test services', description='This is a test description', sort=1)
        self.portfolio = PortfolioCategory.objects.create(name='Test portfolio', sort=1)
        self.photo = Photo.objects.create(sort=1)
        self.team = Team.objects.create(name='Test team', description='This is a test description', sort=1)
        self.contact = Contact.objects.create(name='Test contact', email='test@example.com',
                                              subject='This is a test subject', message='This is a test message')
        self.newsletter = Newsletter.objects.create(email='test@example.com')

    def test_about_model(self):
        self.assertEqual(self.about.name, 'Test about')
        self.assertEqual(self.about.description, 'This is a test description')
        self.assertEqual(self.about.sort, 1)

    def test_services_model(self):
        self.assertEqual(self.services.name, 'Test services')
        self.assertEqual(self.services.description, 'This is a test description')
        self.assertEqual(self.services.sort, 1)

    def test_portfolio_model(self):
        self.assertEqual(self.portfolio.name, 'Test portfolio')
        self.assertEqual(self.portfolio.sort, 1)

    def test_photo_model(self):
        self.assertEqual(self.photo.sort, 1)

    def test_team_model(self):
        self.assertEqual(self.team.name, 'Test team')
        self.assertEqual(self.team.description, 'This is a test description')
        self.assertEqual(self.team.sort, 1)

    def test_contact_model(self):
        self.assertEqual(self.contact.name, 'Test contact')
        self.assertEqual(self.contact.email, 'test@example.com')
        self.assertEqual(self.contact.subject, 'This is a test subject')
        self.assertEqual(self.contact.message, 'This is a test message')

    def test_newsletter_model(self):
        self.assertEqual(self.newsletter.email, 'test@example.com')


# views tests
class ViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view_get(self):
        About.objects.create(name='About us', description='About description', sort=1)
        Services.objects.create(name='Service 1', description='Service description', sort=1)
        PortfolioCategory.objects.create(name='PortfolioCategory 1', sort=1)
        Photo.objects.create(sort=1)
        Team.objects.create(name='Team 1', description='Team description', sort=1)

        request = self.factory.get(reverse('main:index'))
        response = IndexView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('about' in response.context_data)
        self.assertTrue('services' in response.context_data)
        self.assertTrue('categories' in response.context_data)
        self.assertTrue('photo' in response.context_data)
        self.assertTrue('team' in response.context_data)
        self.assertTrue('form' in response.context_data)
        self.assertTrue('newsletter' in response.context_data)

    def test_index_view_post_contact_form_valid(self):
        data = {'submit_contact_form': 'submit', 'name': 'Test user', 'email': 'test@example.com',
                'subject': 'This is a test subject', 'message': 'This is a test message'}
        response = self.client.post(reverse('main:index'), data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Thank you!')

    def test_index_view_post_newsletter_form_valid(self):
        data = {'submit_newsletter': 'submit', 'email': 'test@example.com'}
        response = self.client.post(reverse('main:index'), data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('newsletter' in response.context)


# form tests
class ContactFormTestCase(TestCase):
    def test_contact_form_valid(self):
        data = {'name': 'Test user', 'email': 'test@example.com',
                'subject': 'This is a test subject', 'message': 'This is a test message'}
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid(self):
        data = {'name': '', 'email': 'invalid_email', 'subject': '', 'message': ''}
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())


class NewsletterFormTestCase(TestCase):
    def test_newsletter_form_valid(self):
        data = {'email': 'test@example.com'}
        form = NewsletterForm(data=data)
        self.assertTrue(form.is_valid())

    def test_newsletter_form_invalid(self):
        data = {'email': 'invalid_email'}
        form = NewsletterForm(data=data)
        self.assertFalse(form.is_valid())
