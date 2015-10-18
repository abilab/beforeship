from django.db import models


PAYMENT_STATUS = (
    ("CANC", "Canceled"),
    ("PEND", "Pending"),
    ("PARTLY_PAID", "Partly Paid"),
    ("PAID", "Paid")
)


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    backer_id = models.IntegerField()
    first_name = models.CharField(max_length=256, blank=False)
    last_name = models.CharField(max_length=256, blank=False)
    email = models.EmailField(blank=False)
    order_date = models.CharField(max_length=256, blank=False)
    reward = models.TextField(blank=False)
    notes = models.TextField(blank=True)
    financial_status = models.CharField(max_length=256, choices=PAYMENT_STATUS)
    mail_receipt_status = models.BooleanField(default=False)
    mail_receipt_path = models.FilePathField(path='.')
    customer_data_confirmed = models.BooleanField(default=False)  # Needed?
    billing_delivery_requested = models.BooleanField(default=False)
    same_billing_and_shipping_address = models.BooleanField(default=True)

    # Next shipping_ fields belongs to "Shipping Address"
    shipping_first_name = models.CharField(max_length=256, blank=False)
    shipping_last_name = models.CharField(max_length=256, blank=False)
    shipping_company = models.CharField(max_length=256, blank=True)
    shipping_address_1 = models.CharField(max_length=50, blank=False)
    shipping_address_2 = models.CharField(max_length=50, blank=True, null=True)
    shipping_city = models.CharField(max_length=256, blank=False)
    shipping_country = models.CharField(max_length=256, blank=False)
    shipping_state = models.CharField(max_length=256, blank=True)
    shipping_postal_code = models.CharField(max_length=10, blank=False)
    shipping_phone = models.CharField(max_length=20, blank=True)

    # Next billing_ fields belongs to "Billing Address"
    billing_first_name = models.CharField(max_length=256, blank=False)
    billing_last_name = models.CharField(max_length=256, blank=False)
    billing_company = models.CharField(max_length=256, blank=True)
    billing_address_1 = models.CharField(max_length=50, blank=False)
    billing_address_2 = models.CharField(max_length=50, blank=True, null=True)
    billing_city = models.CharField(max_length=256, blank=False)
    billing_country = models.CharField(max_length=256, blank=False)
    billing_state = models.CharField(max_length=256, blank=True)
    billing_postal_code = models.CharField(max_length=10, blank=False)
    billing_phone = models.CharField(max_length=20, blank=True)
