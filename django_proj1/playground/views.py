from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 
from django.shortcuts import redirect
from playground.forms import LogMessageForm
from playground.models import LogMessage
#in here we buildthe code that is going to serve  http requests

def log_message (request) :
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "playground/log_message.html", {"form": form})

def say_hello (request) :
    return HttpResponse('Hello World')
def hello_there (request, name) :
    return render(
        request,
        'playground/hello_there.html',
        {
            'name':name,
            'date':datetime.date.today
        }
    )

def home (request) :
    return render (request, "playground/home.html")

def about (request) :
    return render (request, "playground/about.html")

def contact (request) :
    return render (request,"playground/contact.html")