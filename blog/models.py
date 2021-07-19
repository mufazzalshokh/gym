from django.db import models
from django.utils.translation import ugettext_lazy as _


class CategoryModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class GalleryModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    image = models.ImageField(upload_to='image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')


class GalleryBannerModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    image = models.ImageField(upload_to='cover', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))


class BlogBannerModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    image = models.ImageField(upload_to='cover', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
