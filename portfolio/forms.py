from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """
    User model contact for enquires.
    """
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Kerry John'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'kerry@example.com.'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 5, 
            'placeholder': 'Enter your message here...'}))

    class Meta:
        model = Contact
        fields = [
            'name', 'email', 'subject', 'message'
            ]