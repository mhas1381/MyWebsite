from django import forms
from website.models import Contact , NewsLetter
from captcha.fields import CaptchaField

class Contact_Form(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'

class NewsLetter_Form(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = NewsLetter
        fields = '__all__'