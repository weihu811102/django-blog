from django.shortcuts import render
from blog.models import Blog, Category
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world")
    blogs = Blog.objects.all()
    return render(request, "index.html", locals())
