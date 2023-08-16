from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogListViews, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('', cache_page(60)(BlogListViews.as_view()), name='blog_list'),
    path('<int:pk>', cache_page(60)(BlogDetailView.as_view()), name='blog_detail'),

]
