from django.db import models
from django.utils.translation import ugettext_lazy as _


class ContactModel(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=50, verbose_name=_('last_name'))
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))
    subject = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


class BannerModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    image = models.ImageField(upload_to='cover', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'


class TypeModel(models.Model):
    title = models.CharField(max_length=30)
    short_description = models.TextField(verbose_name=_('short_description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return str(self.title)


class ExpertModel(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image', verbose_name=_('image'))
    job_expert = models.CharField(max_length=15, verbose_name=_('job_expert'))
    short_description = models.TextField(verbose_name=_('short_description'))

    def __str__(self):
        return self.title
