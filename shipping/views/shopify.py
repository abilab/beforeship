from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import FormView
from shipping.shopify_container.shopify_agent_container import ShopifyAgent
from shipping.forms.shopify import ShopifyInputForm
from shipping.models import Shops, ShopSources

class Shopify():
    @classmethod
    def _set_shopify_agent(cls, shop_name):
        cls.shopify_agent = ShopifyAgent(shop_name)


class ShopifyInputView(FormView, Shopify):
    template_name = "shopify/shopify_input.html"
    form_class = ShopifyInputForm
    success_url = "/shopify/test/"

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            self.__class__.__bases__[1]._set_shopify_agent(form.cleaned_data['shop_name'])
            self.shopify_agent.setup_session()
            self.shopify_agent.setup_permission_url()
            return HttpResponseRedirect(self.shopify_agent.permission_url)
        else:
            return self.form_invalid(form)


class TestShopify(TemplateView, Shopify):
    template_name = 'shopify/test_shopify.html'

    def get(self, request):
        params = {key: request.GET.get(key) for key in\
                  ['code', 'shop', 'signature', 'timestamp', 'hmac']}
        self.shopify_agent.set_token(params)
        new_shop = Shops(owner=self.request.user,
                         shop_source=ShopSources.objects.get(source="Shopify"),
                         shop_name=self.shopify_agent.shop_name,
                         token=self.shopify_agent.token)
        new_shop.save()
        return super().get(request)


# class ShopifyGetCode(Shopify):
#     def get(self, request):
#         self.__class__.__bases__[0]._set_shopify_agent('teststore-1109')
#         self.shopify_agent.set_permission_url()
#         return render(request, 'shopify/shopify_connect.html',
#                       {'shopify_agent': self.shopify_agent})
# 
# 
# class ShopifyGetToken(Shopify):
#     def get(self, request):
#         params = {key: request.GET.get(key) for key in\
#                     ['code', 'shop', 'signature', 'timestamp', 'hmac']}
#         self.shopify_agent._set_token(params)
#         self.shopify_agent.fetch_orders()
#         return render(request, 'shopify/shopify_callback.html',
#                       {'orders': self.shopify_agent.transformed_orders_list})
