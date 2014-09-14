from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from blog.models import Blog

urlpatterns = patterns("",
        #url(r"^$", 'blog.views.index', name='index'), 
        url(r"^$", ListView.as_view(queryset=Blog.objects.all(), context_object_name="blogs", template_name="blog/index.html"), name="index"),
        url(r"^(?P<pk>\d+)/detail/$", DetailView.as_view(model=Blog, template_name="blog/blog_detail.html", context_object_name="blog"), name="detail"),
        )
