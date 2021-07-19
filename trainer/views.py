from django.views.generic import ListView

from trainer.models import PriceModel, MasterModel, TrainerBannerModel, PriceBannerModel


class PriceListView(ListView):
    template_name = 'pricing.html'
    queryset = PriceModel.objects.order_by('-pk')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PriceListView, self).get_context_data(**kwargs)
        context['banners'] = PriceBannerModel.objects.all()
        return context


class MasterListView(ListView):
    template_name = 'about.html'
    queryset = MasterModel.objects.order_by('-pk')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MasterListView, self).get_context_data(**kwargs)
        context['banners'] = TrainerBannerModel.objects.all()
        return context
