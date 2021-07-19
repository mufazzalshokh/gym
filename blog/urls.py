from django.urls import path

from blog.views import GalleryListView, BlogListView

app_name = 'blog'

urlpatterns = [
    path('gallery/', GalleryListView.as_view(), name='list'),
    path('', BlogListView.as_view(), name='blog')
]
