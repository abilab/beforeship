from django.db import models


PAYMENT_STATUS = (
    ("CANC", "Canceled"),
    ("PEND", "Pending"),
    ("PARTLY_PAID", "Partly Paid"),
    ("PAID", "Paid")
)


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=256, blank=False)
    last_name = models.CharField(max_length=256, blank=False)
    email = models.EmailField(blank=False)
    order_date = models.CharField(max_length=256, blank=False)
    order_confirmed = models.BooleanField()
    reward = models.TextField(blank=False)
    notes = models.TextField(blank=True)
    financial_status = models.CharField(max_length=256, choices=PAYMENT_STATUS)
    mail_receipt_status = models.BooleanField(default=False)
    mail_receipt_path = models.FilePathField(path='.')
    customer_data_confirmed = models.BooleanField(default=False)

    # Next shipping_ fields belongs to "Delivery Address"
    shipping_country = models.CharField(max_length=256, blank=False)
    shipping_province = models.CharField(max_length=256, blank=True)
    shipping_province_code = models.CharField(max_length=256, blank=True)
    shipping_zip = models.CharField(max_length=10, blank=False)
    shipping_city = models.CharField(max_length=256, blank=False)
    shipping_address_1 = models.CharField(max_length=256, blank=False)
    shipping_address_2 = models.CharField(max_length=256, blank=True)
    shipping_first_name = models.CharField(max_length=256, blank=False)
    shipping_last_name = models.CharField(max_length=256, blank=False)
    shipping_company = models.CharField(max_length=256, blank=True)
    shipping_phone = models.CharField(max_length=20, blank=True)

    # Next billing_ fields belongs to "Billing Address"
    billing_country = models.CharField(max_length=256, blank=False)
    billing_province = models.CharField(max_length=256, blank=True)
    billing_province_code = models.CharField(max_length=256, blank=True)
    billing_zip = models.CharField(max_length=10, blank=False)
    billing_city = models.CharField(max_length=256, blank=False)
    billing_address_1 = models.CharField(max_length=256, blank=False)
    billing_address_2 = models.CharField(max_length=256, blank=True)
    billing_first_name = models.CharField(max_length=256, blank=False)
    billing_last_name = models.CharField(max_length=256, blank=False)
    billing_company = models.CharField(max_length=256, blank=True)
    billing_phone = models.CharField(max_length=20, blank=True)

    billing_delivery_requested = models.BooleanField(default=False)
    same_billing_and_shipping_address = models.BooleanField(default=True)
