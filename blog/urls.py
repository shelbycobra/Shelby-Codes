
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'index.html', views.index, name="index"),
    url(r'projects.html', views.view_projects, name="projects"),
    url(r'blog_main.html', views.blog_main, name="blog_main"),
    url(r'about.html', views.about, name="about"),
    url(r'cat/(?P<slug>[^\.]+).html', views.view_category, name="category"),
    url(r'^(?P<slug>[^\.]+).html', views.view_post, name="post"),

]