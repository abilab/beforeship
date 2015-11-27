"""beforeship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from shipping.views.shopify import ShopifyInputView, TestShopify
from shipping.views.csv import CSVInputView
from shipping.views.registration import LoginView, LogoutView, AddUserView, UserProfile
from shipping.views.user_data import UserView
from shipping.views.basic import HomeView, ShopSourcesView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Home view
    url(r'^$', HomeView.as_view(), name='home'),

    #basic views
    url(r'^shop/sources', ShopSourcesView.as_view(), name='shop_sources'),

    # Shopify views
    url(r'^shopify/input', ShopifyInputView.as_view(), name='shopify_input'),
#     url(r'^shopify/connect', ShopifyGetCode.as_view(), name='shopify_connect'),
#     url(r'^shopify/callback', ShopifyGetToken.as_view(), name='shopify_callback'),
    url(r'^shopify/test', TestShopify.as_view(), name='test_shopify'),

    # CSV views
    url(r'^csv/input', CSVInputView.as_view(), name='csv_input'),

    # User registration views
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^registration/', AddUserView.as_view(), name='add_user'),
    url(r'^user/profile/', UserProfile.as_view(), name='user_profile'),

    # User data views
    url(r'^user/home/', UserView.as_view(), name='user_home')
]
