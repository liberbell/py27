from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

post = [
    {
        'author': 'Bob',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 25, 2019'
    }
]

def business(request):
    return render(request, "blog/business.html")