from django.urls import reverse
from django.views.generic import CreateView, TemplateView

from pages.forms import ContactModelForm
from pages.models import BannerModel


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('contact:contact')


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['banners'] = BannerModel.objects.order_by('pk')
        return context
