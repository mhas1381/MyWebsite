from django.forms import ModelForm
from website.models import Contact

class Contact_Form(ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'