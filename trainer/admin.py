from django.contrib import admin

from trainer.models import PriceModel, MasterModel, TrainerBannerModel, PriceBannerModel


@admin.register(PriceModel)
class PriceModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', ]
    list_filter = ['created_at']
    search_fields = ['title', 'short_description']
    readonly_fields = ['real_price']


@admin.register(MasterModel)
class MasterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'job', 'created_at', ]
    list_filter = ['created_at']
    search_fields = ['name', 'created_at']


@admin.register(TrainerBannerModel)
class TrainerBannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(PriceBannerModel)
class PriceBannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
