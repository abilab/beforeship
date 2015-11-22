from django import forms


class ShopifyInputForm(forms.Form):
    shop_name = forms.CharField(label="your shop name in Shopify service",
                                error_messages={"required":
                                                "please enter correct name of"
                                                " your shop in Shopify "
                                                "service"})
