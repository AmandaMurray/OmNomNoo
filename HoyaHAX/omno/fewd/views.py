from django.shortcuts import render

def index(request):
    return render(request, "fewd/index.html")
# Create your views here.
