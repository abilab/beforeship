# Shopify Application Credentials
API_KEY = '098a9777d70067f5f487792711fb1b06'
SHARED_SECRET = '1ab1f7b9a1eb2271ed17212eee892454'
# Shopify Properties for Addresses in Orders List
ORDER_PROP_DICT = {'billing_address': ['address1', 'address2', 'city',
                                       'company', 'country', 'first_name',
                                       'id', 'last_name', 'phone', 'province',
                                       'zip', 'name', 'province_code',
                                       'country_code', 'default'],
                   'customer': ['accepts_marketing', 'created_at', 'email',
                                'first_name', 'id', 'last_name', 'note',
                                'orders_count', 'state', 'total_spent',
                                'updated_at', 'tags'],
                   'line_items': ['fulfillable_quantity',
                                  'fulfillment_service', 'fulfillment_status',
                                  'grams', 'price', 'product_id', 'quantity',
                                  'requires_shipping', 'sku', 'title',
                                  'variant_id', 'variant_title', 'vendor',
                                  'name', 'gift_card', 'taxable', 'tax_lines',
                                  'total_discount'],
                   'shipping_address': ['address1', 'address2', 'city',
                                        'company', 'country', 'first_name',
                                        'last_name', 'latitude', 'longitude',
                                        'phone', 'province', 'zip', 'name',
                                        'country_code', 'province_code']}
