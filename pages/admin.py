from django.contrib import admin

from pages.models import ContactModel, BannerModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'message', 'subject']
    search_fields = ['first_name', 'last_name', 'email', 'message']
    list_filter = ['created_at']


@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['created_at']




