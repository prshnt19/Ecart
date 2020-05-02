from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost 

# Create your views here.
def index(request):
    blogposts = Blogpost.objects.all()
    n = len(blogposts)
    return render(request, 'blog/index.html', {'blogposts':blogposts,'count':n})
def blogpost(request,myid):
    blogpost = Blogpost.objects.filter(post_id=myid)
    return render(request, 'blog/blogpost.html', {'blogpost':blogpost[0]}) 