from django import forms
from .models import Contact, Newsletter


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'id': 'subject', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Message'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }
        help_texts = {
            'email': 'example@example.com',
        }
        error_messages = {
            'name': {'required': 'Please enter your name'},
            'email': {'required': 'Please enter your email'},
            'subject': {'required': 'Please enter your subject'},
            'message': {'required': 'Please enter your message'},
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Your Email'}),
        }
        labels = {'email': 'Email'}
        help_texts = {'email': 'example@example.com'}
        error_messages = {'email': {'required': 'Please enter your email'}}

    def clean_email(self):
        email = self.cleaned_data['email']
        return email
