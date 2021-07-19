from django.urls import path

from pages.views import ContactCreateView, HomeTemplateView

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('', HomeTemplateView.as_view(), name='home'),
]
