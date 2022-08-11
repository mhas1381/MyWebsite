from django.shortcuts import render
from website.models import Contact
from website.forms import Contact_Form
from django.contrib import messages
# Create your views here.
def index_view(request):
    return render(request,'website/index.html')
def contact_view(request):
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            form.save()
    form = Contact_Form()
    return render(request,'website/contact.html',{'form':form})