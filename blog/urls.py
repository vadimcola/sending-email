from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListViews

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListViews.as_view(), name='blog_list'),
]
