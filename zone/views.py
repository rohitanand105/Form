from datetime import datetime
from django.shortcuts import render, HttpResponse
from zone.models import Form

def home(request):
    return render(request, 'home.html')    

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def form(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        # dob = request.POST.get('dob')
        # dob = None
        form = Form(fname = fname, lname = lname, email = email, date = datetime.today() )
        form.save()
    return render(request, 'form.html')

# Create your views here.
