from django import forms
from django.forms.utils import ErrorList
from .models import Contact


class ContactForm(forms.ModelForm):
    def __init__(
            self,
            data=None,
            files=None,
            auto_id="id_%s",
            prefix=None,
            initial=None,
            error_class=ErrorList,
            label_suffix=None,
            empty_permitted=False,
            instance=None,
            use_required_attribute=None,
            renderer=None,
    ):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)
        self.cleaned_data = None

    def clean(self):
        self.cleaned_data = super().clean()

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
            'name': 'name',
            'email': 'email',
            'subject': 'subject',
            'message': 'message',
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








