from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PriceTipModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    price = models.FloatField(verbose_name=_('price'))
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('price tip')
        verbose_name_plural = _('price tips')


class PriceModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(verbose_name=_('real price'), default=0)
    discount = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ], verbose_name=_('discount')
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))


class PriceBannerModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    image = models.ImageField(upload_to='cover', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))


class MasterModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    avatar = models.ImageField(upload_to='avatar', verbose_name=_('avatar'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    job = models.CharField(max_length=50, verbose_name=_('job'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class TrainerBannerModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    image = models.ImageField(upload_to='cover', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
