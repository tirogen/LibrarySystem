from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kargs):
    context = {
        "text" : "god"
    }
    return render(request, "student.html", context)
    #return HttpResponse("<h1>test</h1>")
