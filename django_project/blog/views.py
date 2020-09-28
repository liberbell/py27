from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def business(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, "blog/business.html", context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/business.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post