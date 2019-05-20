from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'VaniS',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'May 19, 2019'
    },
    {
        'author': 'Jack Sparrow',
        'title': 'Pirates of Carribean',
        'content': 'The curse of the black pearl',
        'date_posted': 'May 20, 2019'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
