from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    context = {
        "name": "joe",
        "age": 35
    }
    return render(request, 'leads/home_page.html', context)