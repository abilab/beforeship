from django.shortcuts import render
from shipping.shopify_container.shopify_agent_container import ShopifyAgent
from django.views.generic.base import View
from shipping.models import Order


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
        params = {key: request.GET.get(key) for key in
                  ['code', 'shop', 'signature', 'timestamp', 'hmac']}
        self.shopify_agent._set_token(params)
        self.shopify_agent.fetch_orders()
        for o in self.shopify_agent.transformed_orders_list:
            order = Order(
                order_id=o["order_id"],
                backer_id=o["backer_id"],
                first_name=o["first_name"],
                last_name=o["last_name"],
                email=o["email"],
                order_date=o["order_date"],
                financial_status=o["financial_status"],
                reward=o["reward"],
                shipping_first_name=o["shipping_address"]["first_name"],
                shipping_last_name=o["shipping_address"]["last_name"],
                shipping_company=o["shipping_address"]["company"],
                shipping_address_1=o["shipping_address"]["address1"],
                shipping_address_2=o["shipping_address"]["address2"],
                shipping_city=o["shipping_address"]["city"],
                shipping_country=o["shipping_address"]["country"],
                shipping_state=o["shipping_address"]["state"],
                shipping_postal_code=o["shipping_address"]["postal_code"],
                shipping_phone=o["shipping_address"]["telephone"],

                billing_first_name=o["billing_address"]["first_name"],
                billing_last_name=o["billing_address"]["last_name"],
                billing_company=o["billing_address"]["company"],
                billing_address_1=o["billing_address"]["address1"],
                billing_address_2=o["billing_address"]["address2"],
                billing_city=o["billing_address"]["city"],
                billing_country=o["billing_address"]["country"],
                billing_state=o["billing_address"]["state"],
                billing_postal_code=o["billing_address"]["postal_code"],
                billing_phone=o["billing_address"]["telephone"],

                same_billing_and_shipping_address=True if
                o["shipping_address"] == o["billing_address"] else False)
            order.save()
        return render(request, 'shopify_callback.html',
                      {'orders': self.shopify_agent.transformed_orders_list})
