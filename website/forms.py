from django import forms
from website.models import Contact , NewsLetter

class Contact_Form(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

class NewsLetter_Form(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = NewsLetter
        fields = '__all__'