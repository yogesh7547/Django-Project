from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("hello world chai aur django home page")
    return render(request, "website/index.html")

def about(request):
    #return HttpResponse("this is the about section of this website")
    return render(request, "website/about.html")

def contact(request):
    #return HttpResponse("you can contact us here")
    return render(request, "website/contact.html")

 