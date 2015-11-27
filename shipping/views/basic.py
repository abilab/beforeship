from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def csrf_failure(request, reason=""):
    return HttpResponseRedirect(reverse('login'))

class HomeView(TemplateView):
    template_name = 'basic/home.html'

class ShopSourcesView(TemplateView):
    template_name = 'basic/shop_sources.html'
