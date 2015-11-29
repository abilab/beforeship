from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from shipping.forms.csv import CSVInputForm
from shipping.csv_container.csv_agent_container import CSVFile
from shipping.models import Shops, Order, ShopSources
import csv


class CSVInputView(FormView):
    template_name = "csv/csv_input.html"
    form_class = CSVInputForm
    success_url = "user/home"

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        self.form = self.get_form()
        if self.form.is_valid():
            if self._verify_shop():
                self.csv_file = CSVFile(request.FILES["csv_file"],
                                        self.form.cleaned_data["shop_name"])
                self.csv_file.process_csv_file()
                self._save_orders()
                messages.info(request, ("Your shop has connected to service "
                                        "successfully, all orders have been "
                                        "fetched from file"))
            else:
                messages.info(request, ("Shop is already exist. Try another "
                                        "name for shop or delete existing"))
            return HttpResponseRedirect(reverse("user_home"))
        return self.form_invalid(self.form)

    def _verify_shop(self):
        self.shop, created = (Shops.objects.get_or_create
                              (owner=self.request.user,
                               shop_source=\
                                ShopSources.objects.get(source="CSV"),
                               shop_name=self.form.\
                                cleaned_data["shop_name"],
                               token=""))
        if created:
            return True
        return False

    def _save_orders(self):
        for order in self.csv_file.file_content_list:
            (Order.objects.create
                          (shop_id=self.shop,
                           backer_id=order["backer_id"],
                           first_name=order["first_name"],
                           last_name=order["last_name"],
                           email=order["email"],
                           order_date=order["order_date"],
                           reward=order["reward"],
                           notes=order["notes"],
                           financial_status=order["financial_status"],
                           shipping_first_name=order["shipping_first_name"],
                           shipping_last_name=order["shipping_last_name"],
                           shipping_company=order["shipping_company"],
                           shipping_address_1=order["shipping_address_1"],
                           shipping_address_2=order["shipping_address_2"],
                           shipping_city=order["shipping_city"],
                           shipping_country=order["shipping_country"],
                           shipping_state=order["shipping_state"],
                           shipping_postal_code=order["shipping_postal_code"],
                           shipping_phone=order["shipping_phone"],
                           billing_first_name=order["billing_first_name"],
                           billing_last_name=order["billing_last_name"],
                           billing_company=order["billing_company"],
                           billing_address_1=order["billing_address_1"],
                           billing_address_2=order["billing_address_2"],
                           billing_city=order["billing_city"],
                           billing_country=order["billing_country"],
                           billing_state=order["billing_state"],
                           billing_postal_code=order["billing_postal_code"],
                           billing_phone=order["billing_phone"]))
