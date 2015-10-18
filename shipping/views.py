from django.shortcuts import render
from shipping.shopify_container.shopify_agent_container import ShopifyAgent
from django.views.generic.base import View

class Shopify(View):
    @classmethod
    def _set_shopify_agent(cls, shop_name):
        cls.shopify_agent = ShopifyAgent(shop_name)


class ShopifyGetCode(Shopify):
    def get(self, request):
        self.__class__.__bases__[0]._set_shopify_agent('teststore-1109')
        self.shopify_agent._set_permission_url()
        return render(request, 'home.html',
                      {'shopify_agent': self.shopify_agent})


class ShopifyGetToken(Shopify):
    def get(self, request):
        params = {key: request.GET.get(key) for key in\
                    ['code', 'shop', 'signature', 'timestamp', 'hmac']}
        self.shopify_agent._set_token(params)
        self.shopify_agent.fetch_orders()
        return render(request, 'shopify_callback.html',
                      {'orders': self.shopify_agent.transformed_orders_list})
