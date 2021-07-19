from django.urls import path

from trainer.views import PriceListView, MasterListView

app_name = 'trainer'

urlpatterns = [
    path('price/', PriceListView.as_view(), name='price'),
    path('about/', MasterListView.as_view(), name='master'),
]
