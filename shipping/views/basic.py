from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'basic/home.html'

class ShopSourcesView(TemplateView):
    template_name = 'basic/shop_sources.html'
