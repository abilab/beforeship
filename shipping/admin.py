from django.contrib import admin
from shipping.models import Order, Shops, ShopSources

admin.site.register(Order)
admin.site.register(Shops)
admin.site.register(ShopSources)
