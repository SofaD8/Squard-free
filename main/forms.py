from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    def save(self, commit=True):
        contact = super().save(commit=False)
        contact.name = self.cleaned_data['name'].title()
        if commit:
            contact.save()
        return contact

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
