from django.views.generic import ListView

from blog.models import GalleryModel, GalleryBannerModel
from pages.models import BannerModel


class GalleryListView(ListView):
    template_name = 'gallery.html'

    def get_queryset(self):
        return GalleryModel.objects.order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['banners'] = GalleryBannerModel.objects.all()
        return context


class BlogListView(ListView):
    template_name = 'blog.html'

    def get_queryset(self):
        return BlogModel.objects.order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['banners'] = BannerModel.objects.all()
        return context
