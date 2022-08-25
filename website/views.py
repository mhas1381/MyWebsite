from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from website.models import Contact
from website.forms import Contact_Form, NewsLetter_Form
from django.contrib import messages
# Create your views here.
def index_view(request):
    return render(request,'website/index.html')
def contact_view(request):
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = Contact_Form()
    return render(request,'website/contact.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetter_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')