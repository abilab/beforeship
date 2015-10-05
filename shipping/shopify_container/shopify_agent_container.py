import shopify
from shipping.shopify_container.config import (API_KEY,
                                               SHARED_SECRET)

class ShopifyAgent():
    def __init__(self, shop_name):
        self.shop_name = shop_name

    def _set_permission_url(self):
        shopify.Session.setup(api_key=API_KEY, secret=SHARED_SECRET)
        self.session = shopify.Session(self.shop_name + '.myshopify.com')
        self.scope = ['read_content', 'write_content',
                      'read_products', 'write_products',
                      'read_customers', 'write_customers',
                      'read_orders', 'write_orders',
                      'read_shipping', 'write_shipping']
        self.permission_url = self.session.\
            create_permission_url(self.scope,
                                  'http://127.0.0.1:8000/shopify/callback')

    def _set_token(self, params):
        self.token = self.session.request_token(params)
        self.session = shopify.Session(self.shop_name + '.myshopify.com',
                                       self.token)

    def fetch_customers(self):
        shopify.ShopifyResource.activate_session(self.session)
        customers_attrs = []
        customers_list = shopify.Customer.search()
        for customer in customers_list:
            customers_attrs.append(customer.attributes)
        return customers_attrs
