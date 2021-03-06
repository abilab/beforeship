import shopify
from shipping.shopify_container.config import (API_KEY,
                                               SHARED_SECRET)
from beforeship.settings import PORTAL_URL


class ShopifyAgent():
    def __init__(self, shop_name):
        self.shop_name = shop_name

    def setup_session(self):
        shopify.Session.setup(api_key=API_KEY, secret=SHARED_SECRET)
        self.session = shopify.Session(self.shop_name + '.myshopify.com')

    def setup_permission_url(self):
        self.scope = ['read_content', 'write_content',
                      'read_products', 'write_products',
                      'read_customers', 'write_customers',
                      'read_orders', 'write_orders',
                      'read_shipping', 'write_shipping']
        self.redirect_uri = PORTAL_URL + r'/shopify/test'
        self.permission_url = self.session.\
            create_permission_url(self.scope, redirect_uri=self.redirect_uri)

    def set_token(self, params):
        self.token = self.session.request_token(params)

    def fetch_orders(self):
        self.session = shopify.Session(self.shop_name + '.myshopify.com',
                                       token=self.token)
        shopify.ShopifyResource.activate_session(self.session)
        self.input_orders_list = []
        self.orders_list_fetched = shopify.Order.find()
        for order in self.orders_list_fetched:
            self.input_orders_list.append(order.to_dict())
        self.transform_orders()

    def transform_orders(self):
        self.transformed_orders_list = []
        for order in self.input_orders_list:
            customer_order = {}
            customer_order['order_id'] = order['id']
            customer_order['backer_id'] = order['customer']['id']
            customer_order['first_name'] = order['customer']['first_name']
            customer_order['last_name'] = order['customer']['last_name']
            customer_order['email'] = order['customer']['email']
            customer_order['order_date'] = order['created_at']
            customer_order['financial_status'] = order['financial_status']  # Nice to have to display on page?
            customer_order['reward'] = [{' '.join([item['name'], 'SKU:', item['sku']]): item['quantity']} for item in order['line_items']]
            customer_order['billing_address'] = {'first_name': order['billing_address']['first_name'],
                                                 'last_name': order['billing_address']['last_name'],
                                                 'company': order['billing_address']['company'],
                                                 'address1': order['billing_address']['address1'],
                                                 'address2': order['billing_address']['address2'],
                                                 'city': order['billing_address']['city'],
                                                 'country': order['billing_address']['country'],
                                                 'state': order['billing_address']['province'],
                                                 'postal_code': order['billing_address']['zip'],
                                                 'telephone': order['billing_address']['phone']}  # Rename to phone?
            customer_order['shipping_address'] = {'first_name': order['billing_address']['first_name'],
                                                  'last_name': order['billing_address']['last_name'],
                                                  'company': order['billing_address']['company'],
                                                  'address1': order['billing_address']['address1'],
                                                  'address2': order['billing_address']['address2'],
                                                  'city': order['billing_address']['city'],
                                                  'country': order['billing_address']['country'],
                                                  'state': order['billing_address']['province'],
                                                  'postal_code': order['billing_address']['zip'],
                                                  'telephone': order['billing_address']['phone']}
            self.transformed_orders_list.append(customer_order)
